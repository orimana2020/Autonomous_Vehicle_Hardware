import numpy as np
import matplotlib.pyplot as plt
from py_Utils import Trajectory, CSpace, inflate



class Plotter():
    def __init__(self, inflated_map): 
        self.env_rows, self.env_cols = inflated_map.shape
        self.map = inflated_map
    
    def draw_graph(self, start=None, goal=None,path=None):
        plt.gcf().canvas.mpl_connect(
            'key_release_event',
            lambda event: [exit(0) if event.key == 'escape' else None])
        
        plt.xlim([0, self.env_cols])
        plt.ylim([0, self.env_rows])
        
        if path is not None:
            for i in range(len(path)-1):
                plt.plot([path[i][0],path[i+1][0]], [path[i][1],path[i+1][1]], color='r', linewidth=3)
        # if trajectory is not None:
            trajectory = Trajectory(dl=0.2, path=path, TARGET_SPEED=0.9)
            # print(len(trajectory.cx))
            for i in range(len(trajectory.cx)-1):
                plt.scatter([trajectory.cx[i],trajectory.cx[i+1]], [trajectory.cy[i],trajectory.cy[i+1]], color='m', linewidth=3)
        if start is not None:
            plt.scatter(start[0], start[1], s=100, c='g')
            plt.scatter(goal[0],goal[1], s=100, c='r')
        plt.imshow(self.map, origin="lower")
        plt.pause(50)
    




map_dict = np.load('new_lab'+'.npy', allow_pickle=True)
resolution =  map_dict.item().get('map_resolution')
origin_x = map_dict.item().get('map_origin_x')
origin_y = map_dict.item().get('map_origin_y')
map_original = map_dict.item().get('map_data')
inflated_map = inflate(map_original, 3)



path_manual_index = [[160,104],[180,140], [162,173],[186,214],[167,255],[99,256],[32,262],[38,196],[63,136], [138,107]]
converter = CSpace(resolution, origin_x=origin_x, origin_y=origin_y, map_shape=map_original.shape)
path_manual_meter = converter.pathindex2pathmeter(path_manual_index)
trajectory = Trajectory(dl=0.2, path=path_manual_meter, TARGET_SPEED=0.9)



if path_manual_meter is not None:
    loops = 5
    looped_path = []
    for idx in range(loops):
        for coords in path_manual_meter:
            looped_path.append([coords[0], coords[1]])


PLOT_SINGLE_LOOP_PATH = False
if PLOT_SINGLE_LOOP_PATH:
    plotter = Plotter(inflated_map)
    plotter.draw_graph(path=path_manual_index)

else:
    trajectory = Trajectory(dl=0.2, path=converter.pathmeter2pathindex(looped_path), TARGET_SPEED=0.9)
    for i in range(len(trajectory.cx)-1):
        plt.plot([trajectory.cx[i],trajectory.cx[i+1]], [trajectory.cy[i],trajectory.cy[i+1]], color='r', linewidth=3)
    np.save('new_lab_loops_meter', looped_path)
    plt.imshow(map_original, origin="lower")
    plt.pause(50)
    

