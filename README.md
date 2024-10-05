# Project description
This projects implements autonomous racing car, in scale 1/10 of Formula 1. The car is equipped with Lidar and encoders for localization and supports various path planning and tracking algorithms.

# Hardware
1. Traxxes Slash 2WD (chassis)
2. Pololu magnetic encoder
3. Slamtec S2 Lidar
4. Pololu 5V regulator 
5. Raspberry Pi 4 Model B 8GB (on-board computer)
6. Arduino Unu (low level controller)
7. Lipo battery

The Raspberry Pi runs Ubuntu 22.04 Mate, with ROS2

# Installtion
## Raspberry Pi
download imager to burn OS to PI
download ubuntu mate for PI 64 from https://ubuntu-mate.org/download/
install ros:https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html

skip: set locale        
setup sources   
install ros2 packages , desktop version         
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

After installtion update TIME and DATE before sudo apt update and upgrade

## Arduino
Burn the low-level code to the Arduino. the code implements PID controller for drive motor, steering commands, and reading of the encoder for odometry. 


## Install Dependencies:

```terminal
sudo apt install ros-humble-xacro ros-humble-joint-state-publisher-gui ros-humble-joint-state-publisher ros-humble-rplidar-ros ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-gazebo-ros2-control joystick jstest-gtk evtest ros-humble-slam-toolbox ros-humble-navigation2 ros-humble-nav2-bringup ros-humble-turtlebot3*  ros-humble-twist-mux ros-humble-twist-stamper

```

```terminal
sudo apt-get install python3-pip
pip install setuptools==58.2.0
sudo apt install python3-serial 
sudo apt install libserial-dev
sudo apt install net-tools
sudo apt install openssh-server
sudo adduser $USER dialout
```

Find robot IP:
connect robot to wifi 
on robot computer - ifconfig -a -> wlan -> inet         
or      
hostname -I     
or      
how to find robot ip - on robot computer ->wifi -> connection information


setting up ssh:
1. sudo apt install openssh-server
2. service ssh status
3. sudo ufw allow ssh
4. ssh 127.0.0.1
5. ip addr
6. ssh robot1@172.20.10.5


# Low level control packages:
pyserial-miniterm -e /dev/ttyACM0 57600
with o - open loop, e- encoders, m-closed loop
run in terminal 
pyserial-miniterm -e /dev/ttyACM0 57600

find path to some serial device:
ls /dev/serial/by-path/

Original low level controller(for differential drive): https://github.com/joshnewans/diffdrive_arduino/tree/humble

Serial communication: https://github.com/joshnewans/serial

Ros arduino bridge:
https://github.com/joshnewans/ros_arduino_bridge.git

sudo chmod 666 /dev/ttyACM0

# low level calibration:
1. drive the car stright, adjust the offset of the steering
2. measure the turning radius and adjust the maximal steering angle 
3. steering angle = atan(wheelbase/turning radius)


# Usage
## Build
```terminal
source /opt/ros/humble/setup.bash       
colocon build --symlink-install 
source install/setup.bash       
```

# Run
Access the robot via SSH, make sure to source:          
```terminal
ssh robot1@192.168.0.102
cd car_hardware
source /opt/ros/humble/setup.bash
source install/setup.bash
```
### Terminal 1: General communication and low level bring-up
```terminal 
ros2 launch rc_car launch_robot.launch.py
```
### Terminal 2: Lidar communication bring-up
```terminal 
ros2 launch rc_car rplidar_s2.launch.py 
```
### Terminal 3: Rviz, Rviz runs on remote computer and *NOT* via ssh!
```terminal
ros2 run rviz2 rviz2 -d src/rc_car/rviz_config/localization.rviz --ros-args -p use_sim_time:=false
```
### Terminal 4: Mapping
```terminal
ros2 launch rc_car online_async_launch.py use_sim_time:=false
```
1. panels -> add new panel -> slam tool box plugin      
2. in rviz add map and set /map to topic, change durability policy TransientLocal       
2. save the map with rviz, serialize the map
3. To store map as numpy array:    
restart         
run with localization and to save the map:   
```terminal   
ros2 run rc_car ros_Get_map_client.py --ros-args -p map_name:=lab_demo
```
After Mapping restart the the robot

### Terminal 4: Localization
```terminal
ros2 launch rc_car localization.launch.py map:=lab_demo.yaml use_sim_time:=false
```
1. in rviz, manually write "map" in fixed frame
2. change set initial position
3. add map
4. topic->durability policy->transient local


### Terminal 5: Path planning service
```terminal
ros2 run rc_car PathPlanning_service_prm.py --ros-args -p map_name:=map_world -p use_sime_time:=false
```
### Terminal 6: Path planning client
```terminal
ros2 run rc_car PathPlanning_client.py 0 0 6.22 -4.5 path1  --ros-args -p use_sime_time:=false
```
### Terminal 7: Path tracking
NOTE - the path_name without the '_meter'
```terminal
ros2 run rc_car ros_Path_Tracking.py --ros-args -p use_sime_time:=false -p show_path:=true -p show_marker:=true -p path_name:=path1
```



## General
ros2 ros2_control list_hardware_interfaces

How to stop the lidar?  
ros2 launch rc_car rplidar.launch.py     
ros2 service call /stop_motor std_srvs/srv/Empty "{}"           
ros2 service call /start_motor std_srvs/srv/Empty "{}"          

How to remap
ros2 run teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstampted

