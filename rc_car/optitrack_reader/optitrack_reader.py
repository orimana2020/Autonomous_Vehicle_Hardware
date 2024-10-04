import csv
import numpy as np
import matplotlib.pyplot as plt
from py_Utils import Trajectory


def convert_meter2mm(trajectory: Trajectory):
    for i in range(len(trajectory_meter.cx)):
        trajectory.cx[i] = trajectory.cx[i] 
        trajectory.cy[i] = trajectory.cy[i] 
    return trajectory

def fix_coords(map_name, trajectory_mm):
    map_dict = np.load(map_name+'.npy', allow_pickle=True)
    resolution =  map_dict.item().get('map_resolution')
    origin_x = map_dict.item().get('map_origin_x') 
    print(origin_x)  
    origin_y = map_dict.item().get('map_origin_y')
    print(origin_y)
    map_ = map_dict.item().get('map_data')
    for i in range(len(trajectory_mm.cx)):
        trajectory_mm.cx[i] = trajectory_mm.cx[i]# - origin_x * 1000
        trajectory_mm.cy[i] = trajectory_mm.cy[i] #- origin_y * 1000
    return trajectory_mm


# frame, time, rotx, roty, rotz, rotw, rb_x, rgb_y, rb_z
optitrack_data = []
with open('lab_demo.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if 7000>line_count >= 7:
            frame, time, rotx, roty, rotz, rotw, rb_x, rgb_y, rb_z = row[:9]
            optitrack_data.append([int(frame), float(time), float(rotx), float(roty), float(rotz), float(rotw), float(rb_x), float(rgb_y), float(rb_z)])
        line_count +=1 
    print(f'Processed {line_count} lines.')


np.save('car_data', optitrack_data)
optitrack_data = np.load('car_data.npy')


fig = plt.figure()
ax = fig.add_subplot()
ax.scatter(optitrack_data[:,6], -optitrack_data[:,7], c='b')

planned_path = np.load('path_lab_demo_meter.npy')
trajectory_meter = Trajectory(dl=0.01, path=planned_path)
trajectory_mm = convert_meter2mm(trajectory_meter)
trajectory_mm = fix_coords('lab_g2', trajectory_mm)



ax.scatter(trajectory_mm.cx, trajectory_mm.cy, c='r')
plt.axis('equal')
ax.set_xlabel('x [meter]')
ax.set_ylabel('y [meter]')
ax.legend(['OptiTrack', 'Planned Trajectory'])
plt.show()