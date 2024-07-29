import numpy as np
import matplotlib.pyplot as plt
from py_Utils import Trajectory, CSpace, inflate


# path = np.load('path3_meter.npy')
path = [

[69,30],
[106,27],
[145, 26],
[146,48],
[130,70],
[84,70],
[53, 67],
[53,30],
]

if path is not None:
    loops = 5
    looped_path = []
    for idx in range(loops):
        for coords in path:
            looped_path.append([coords[0], coords[1]])
# np.save('path33_meter', np.array(looped_path))
# print(len(path))
# print(len(looped_path))
map_dict = np.load('lab307'+'.npy', allow_pickle=True)
resolution =  map_dict.item().get('map_resolution')
origin_x = map_dict.item().get('map_origin_x')
origin_y = map_dict.item().get('map_origin_y')
map_original = map_dict.item().get('map_data')
map_original = inflate(map_original, 5)


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
                # plt.plot([trajectory.cx[i],trajectory.cx[i+1]], [trajectory.cy[i],trajectory.cy[i+1]], color='m', linewidth=3)
                plt.scatter([trajectory.cx[i],trajectory.cx[i+1]], [trajectory.cy[i],trajectory.cy[i+1]], color='m', linewidth=3)
        if start is not None:
            plt.scatter(start[0], start[1], s=100, c='g')
            plt.scatter(goal[0],goal[1], s=100, c='r')
        plt.imshow(self.map, origin="lower")
        plt.pause(500)




plotter = Plotter(map_original)
if path is not None:
    converter = CSpace(resolution, origin_x=origin_x, origin_y=origin_y, map_shape=map_original.shape )
    print(converter.meter2pixel([0,0]))
    looped_path_meter = converter.pathindex2pathmeter(looped_path)
    np.save('path_lab307_meter', looped_path_meter)
    trajectory = Trajectory(dl=0.2, path=looped_path_meter, TARGET_SPEED=0.9)
    print(len(trajectory.cx))
    plotter.draw_graph(path = looped_path)
else:
    plotter.draw_graph()




