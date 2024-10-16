import numpy as np
import matplotlib.pyplot as plt
from py_Utils import Tree,  CSpace
from py_PurePursuit import PurePersuit_Controller
from py_car_simulator import State, States, Simulator
from py_Utils import Trajectory
import py_car_consts
import math
plt.ion()

class KINORRT(object):
    def __init__(self, env_map, max_step_size = 0.5, max_itr=5000, p_bias = 0.05, converter: CSpace =None ):
        self.max_step_size = max_step_size
        self.max_itr = max_itr
        self.p_bias = p_bias
        self.tree = Tree()
        self.map = env_map
        self.env_rows, self.env_cols = env_map.shape
        self.env_yaw_range = 2*np.pi
        self.converter = converter
        self.ackerman = Odom(converter)
        
        

    def find_path(self, start, goal):
        itr = 0
        self.tree.AddVertex(start)

        while itr < self.max_itr:
            
            # sample random vertex
            x_random = self.sample(goal)

            # find nearest neighbor
            x_near_idx, x_near = self.tree.GetNearestVertex(x_random)
            
            delta_time, steering, velocity = self.ackerman.sample_control_command()
            
            # propagate
            x_new, edge, edge_cost = self.ackerman.propagate(steering, velocity ,delta_time, x_near)
            
            # add vertex and edge
            if self.local_planner(edge):
                x_new_idx = self.tree.AddVertex(x_new)
                self.tree.AddEdge(x_near_idx, x_new_idx, edge_cost)
                self.tree.vertices[x_new_idx].set_waypoints(edge)
                if np.linalg.norm(np.array(x_new[:2])-np.array(goal[:2])) < 10:
                    return self.get_shortest_path(x_new_idx)
            itr += 1
            if itr%1000 ==0:
                print(f'itr: {itr}')
        return None, None, None
    
    def sample(self, goal):
        if np.random.rand() < self.p_bias:
            return goal
        return np.array([np.random.randint(self.env_cols), np.random.randint(self.env_rows), np.pi*2*np.random.rand()])

    
    def is_in_collision(self, x_new):
        if self.map[int(x_new[1])][int(x_new[0])] == 0:
            return False
        return True
    
    def local_planner(self, edge):
        for config in edge:
            if self.is_in_collision(config):
                return False
        return True
    
    def get_shortest_path(self, goal_idx):
        '''
        Returns the path and cost from some vertex to Tree's root
        @param dest - the id of some vertex
        return the shortest path and the cost
        '''
        path_idx = []
        path_idx.append(goal_idx)
        cost = 0
        while path_idx[-1] != 0:
            cost += self.tree.edges[path_idx[-1]]
            path_idx.append(self.tree.edges[path_idx[-1]])
        path = np.array([self.tree.vertices[idx].conf for idx in path_idx][::-1])
        return path, path_idx[::-1] , cost
    
    

class Plotter():
    def __init__(self, inflated_map): 
        self.env_rows, self.env_cols = inflated_map.shape
        self.map = inflated_map
    
    def draw_tree(self, tree:Tree, start, goal, path=None, path_idx = None):
        plt.gcf().canvas.mpl_connect(
            'key_release_event',
            lambda event: [exit(0) if event.key == 'escape' else None])
        plt.xlim([0, self.env_cols])
        plt.ylim([0, self.env_rows])
        if path is not None:
            for idx in path_idx:
                try:
                    vertex = tree.vertices[idx]
                    for waypoint in vertex.waypoints:
                        plt.scatter(waypoint[0], waypoint[1], s=20, c='m')
                except:
                    pass

        for i in range(len(tree.vertices)):
            conf = tree.vertices[i].conf
            plt.scatter(conf[0], conf[1], s=10, c='b')

        
        plt.scatter(start[0], start[1], s=100, c='g')
        plt.scatter(goal[0],goal[1], s=100, c='r')
        plt.imshow(self.map, origin="lower")
        plt.pause(100)
 

    


def inflate(map_, inflation):#, resolution, distance):
    cells_as_obstacle = int(inflation) #int(distance/resolution)
    map_[95:130, 70] = 100
    original_map = map_.copy()
    inflated_map = map_.copy()
    # add berrier
    rows, cols = inflated_map.shape
    for j in range(cols):
        for i in range(rows):
            if original_map[i,j] != 0:
                i_min = max(0, i-cells_as_obstacle)
                i_max = min(rows, i+cells_as_obstacle)
                j_min = max(0, j-cells_as_obstacle)
                j_max = min(cols, j+cells_as_obstacle)
                inflated_map[i_min:i_max, j_min:j_max] = 100
    return inflated_map       
    

class Odom(object):
    def __init__(self, converter:CSpace):
        self.wheelbase = 0.35
        self.max_steering_angle = np.deg2rad(35)
        self.min_velocity, self.max_velocity = 0.5, 1
        self.min_time, self.max_time = 0.5, 1
        self.converter = converter
    
    def sample_control_command(self):
        delta_time = np.random.uniform(low=self.min_time, high=self.max_time)
        steering = np.random.uniform(low=-self.max_steering_angle, high=self.max_steering_angle)
        velocity = np.random.uniform(low=self.min_velocity, high=self.max_velocity)
        return delta_time, steering, velocity

    def propagate(self,  steering, velocity ,delta_time, initial_x):
        initial_x = self.converter.pixel2meter(initial_x)
        x = initial_x[0]
        y = initial_x[1]
        theta= initial_x[2]
        theta_dot = velocity * np.tan(steering) / self.wheelbase
        dt = 0.03
        edge = [[x,y,theta]]
        cost = 0
        for _ in range(int(delta_time/dt)):
            theta += theta_dot * dt
            x_dot = velocity * np.cos(theta)
            y_dot = velocity * np.sin(theta)
            x += x_dot * dt
            y += y_dot * dt
            cost += ((edge[-1][0] - x)**2 + (edge[-1][1] - y)**2)**0.5
            edge.append([x,y,theta])
        edge = self.converter.pathmeter2pathindex(edge)
        new_state = edge[-1]
        return new_state, edge, cost




def main():
    map_dict = np.load('sim_map'+'.npy', allow_pickle=True)
    resolution =  map_dict.item().get('map_resolution')
    origin_x = map_dict.item().get('map_origin_x')
    origin_y = map_dict.item().get('map_origin_y')
    map_original = map_dict.item().get('map_data')
    robot_radius = 0.25
    inflated_map = inflate(map_original, robot_radius/resolution)
    converter = CSpace(resolution, origin_x=origin_x, origin_y=origin_y, map_shape=map_original.shape)
    kinorrt_planner = KINORRT(env_map=inflated_map, max_step_size=20, max_itr=10000, p_bias=0.05,converter=converter )
    # path, path_idx, cost = kinorrt_planner.find_path(start, goal)
    # print(f'cost: {cost}')
    # plotter = Plotter(inflated_map=inflated_map)
    # plotter.draw_tree(kinorrt_planner.tree, start, goal, path, path_idx)


    # PP
    #  hyper-parameters
    k = 0.1  # look forward gain
    Lfc = 1.0  # [m] look-ahead distance
    Kp = 1.0  # speed proportional gain
    dt = 0.1  # [s] time tick
    WB = py_car_consts.wheelbase 
    target_speed = 1.0  # [m/s]
    T = 100.0  # max simulation time
    MAX_STEER = py_car_consts.max_steering_angle_rad  # maximum steering angle [rad]
    MAX_DSTEER = py_car_consts.max_dt_steering_angle  # maximum steering speed [rad/s]
    MAX_SPEED = py_car_consts.max_linear_velocity  # maximum speed [m/s]
    MIN_SPEED = py_car_consts.min_linear_velocity  # minimum speed [m/s]
    MAX_ACCEL = 1.0  # maximum accel [m/ss]

    """
    load path and convert it to trajectory, smooth curve, 
    """
    path = np.load('path3_meter.npy')
    trajectory = Trajectory(dl=0.5, path=path, TARGET_SPEED=target_speed)
    state = State(x=trajectory.cx[0], y=trajectory.cy[0], yaw=trajectory.cyaw[0], v=0.0) # initial state
    if state.yaw - trajectory.cyaw[0] >= math.pi: # initial yaw compensation
        state.yaw -= math.pi * 2.0
    elif state.yaw - trajectory.cyaw[0] <= -math.pi:
        state.yaw += math.pi * 2.0
    lastIndex = len(trajectory.cx) - 1
    time = 0.0
    states = States()
    states.append(time, state)
    pp = PurePersuit_Controller(trajectory.cx, trajectory.cy, k, Lfc, Kp, WB, MAX_ACCEL, MAX_SPEED, MIN_SPEED, MAX_STEER, MAX_DSTEER)
    target_ind, _ = pp.search_target_index(state)
    simulator = Simulator(trajectory, state)
    while  lastIndex > target_ind: #T >= time and
        state.v = pp.proportional_control_acceleration(target_speed, state.v, dt)
        delta, target_ind,_,_ = pp.pure_pursuit_steer_control(state, trajectory, target_ind, dt)
        state.predelta = delta
        simulator.update_state(state, delta)  # Control vehicle
        time += dt
        states.append(time, state, delta)
    simulator.show_simulation(states)

    


if __name__ == "__main__":
    main()


