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
            trajectory = Trajectory(dl=0.5, path=path, TARGET_SPEED=0.9)
            # print(len(trajectory.cx))
            for i in range(len(trajectory.cx)-1):
                plt.scatter([trajectory.cx[i],trajectory.cx[i+1]], [trajectory.cy[i],trajectory.cy[i+1]], color='m', linewidth=3)
        if start is not None:
            plt.scatter(start[0], start[1], s=100, c='g')
            plt.scatter(goal[0],goal[1], s=100, c='r')
        plt.imshow(self.map, origin="lower")
        plt.pause(500)




map_dict = np.load('grant2_demo'+'.npy', allow_pickle=True)
resolution =  map_dict.item().get('map_resolution')
origin_x = map_dict.item().get('map_origin_x')
origin_y = map_dict.item().get('map_origin_y')
map_original = map_dict.item().get('map_data')
# map_original = inflate(map_original, 3)


path = np.load('path_ido_demo_meter.npy') 
if path is not None:
    loops = 5
    looped_path = []
    for idx in range(loops):
        for coords in path:
            looped_path.append([coords[0], coords[1]])





trajectory = Trajectory(dl=0.2, path=looped_path, TARGET_SPEED=0.9)

# plotter.draw_graph(path=looped_path, trajectory=trajectory)
converter = CSpace(resolution, origin_x=origin_x, origin_y=origin_y, map_shape=map_original.shape)

trajectory = Trajectory(dl=0.2, path=converter.pathmeter2pathindex(looped_path), TARGET_SPEED=0.9)
for i in range(len(trajectory.cx)-1):
    plt.plot([trajectory.cx[i],trajectory.cx[i+1]], [trajectory.cy[i],trajectory.cy[i+1]], color='r', linewidth=3)


    
plt.imshow(map_original, origin="lower")
plt.pause(500)

np.save('path_ido_demo_loops_meter', looped_path)

