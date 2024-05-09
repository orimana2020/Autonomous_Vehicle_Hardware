# Autonomous Car
* CRITICAL*
after installtion update TIME and DATE before sudo apt update and upgrade

# building:
source /opt/ros/humble/setup.bash
colocon build --symlink-install
source install/setup.bash


how to stop the lidar?
ros2 launch rc_car rplidar.launch.py 
ros2 service call /stop_motor std_srvs/srv/Empty "{}"
ros2 service call /start_motor std_srvs/srv/Empty "{}"


# --------------------- Real Robot --------------------

ros2 launch rc_car launch_robot.launch.py
ros2 launch rc_car rplidar.launch.py 
ros2 launch rc_car rviz_real_robot.launch.py

mapping:
ros2 launch rc_car online_async_launch.py use_sim_time:=false
1. panels -> add new panel -> slam tool box plugin
2. in rviz add map and set /map to topic, change durability policy TransientLocal
2. save the map with rviz, serialize the map


localiztion:
ros2 launch rc_car localization_launch.py map:=my_lab3.yaml use_sim_time:=false


# ---------- General Notes ---------------------

REAL ROBOT NOTES
download imager to burn OS to PI
download ubuntu mate for PI 64 from https://ubuntu-mate.org/download/




install ros:https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html
        -> skip: set locale
        -> setup sources
        -> install ros2 packages , desktop version



sudo apt install ros-humble-xacro ros-humble-joint-state-publisher-gui ros-humble-joint-state-publisher
sudo apt install ros-humble-rplidar-ros
sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-gazebo-ros2-control
sudo apt install joystick jstest-gtk evtest 
sudo apt install ros-humble-slam-toolbox
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup ros-humble-turtlebot3*
sudo apt install ros-humble-twist-mux 
sudo apt install ros-humble-twist-stamper
sudo apt-get install python3-pip
pip install setuptools==58.2.0
sudo apt install python3-serial 
sudo apt install libserial-dev
sudo adduser $USER dialout

setting up ssh:
1. sudo apt install openssh-server
2. service ssh status
3. sudo ufw allow ssh
4. ssh 127.0.0.1
5. ip addr
6. ssh robot1@172.20.10.5


find path to some serial device:
ls /dev/serial/by-path/

ros2 ros2_control list_hardware_interfaces


how to remap:
ros2 run teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstampted


low level control packages:
1. ros_arduino_bridge - burn to arduino
pyserial-miniterm -e /dev/ttyACM0 57600
with o - open loop, e- encoders, m-closed loop
run in terminal 
pyserial-miniterm -e /dev/ttyACM0 57600


arduino ros bridge:
https://github.com/joshnewans/ros_arduino_bridge.git

add permission to arduino: not needed because of dialout
sudo chmod a+rw /dev/ttyACM0



---- other--- can be ignored----
burn to arduino: https://github.com/joshnewans/ros_arduino_bridge.git

download to src file at the PI:
https://github.com/joshnewans/diffdrive_arduino/tree/humble
https://github.com/joshnewans/serial