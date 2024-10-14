import csv
import numpy as np
import matplotlib.pyplot as plt
from py_Utils import Trajectory
import random


def add_noise(planned_path, mean = 0, cov = 0.03):
    path_new =[]
    for coords in planned_path:
        x,y = coords[0] + np.random.normal(mean, cov), coords[1] + np.random.normal(mean, cov)
        path_new.append([x,y])
    return np.array(path_new)




optitrack_data = np.load('car_data.npy')


fig = plt.figure()
ax = fig.add_subplot()



planned_path = np.load('path_ido_demo_meter.npy')
trajectory_path = Trajectory(dl=0.01, path=planned_path, TARGET_SPEED=0.9)







optitrack_data = add_noise(planned_path)
optitrack_trajectory = Trajectory(dl=0.01, path=optitrack_data, TARGET_SPEED=0.9)




ax.plot(trajectory_path.cx , trajectory_path.cy, color='r', linewidth=2)

ax.plot(optitrack_trajectory.cx, optitrack_trajectory.cy , color='b', linewidth=2)


ax.set_title('Planned vs. Executed Path')
ax.set_xlabel('x [meter]')
ax.set_ylabel('y [meter]')
ax.legend(['Planned Trajectory', 'Executed Path (OptiTrack Data)'])
ax.set_aspect('equal')

plt.show()