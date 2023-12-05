# Autonomous_RC


first install ros2 humble - see documentation 

sudo apt install ros-humble-xacro ros-humble-joint-state-publisher-gui ros-humble-joint-state-publisher

git clone -b humble https://github.com/joshnewans/rc_car.git

sudo apt install ros-humble-rplidar-ros

ros2 ros2_control list_hardware_interfaces


sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-gazebo-ros2-control

git clone -b humble https://github.com/ros-controls/gazebo_ros2_control

sudo apt install joystick jstest-gtk evtest 

sudo apt install ros-humble-slam-toolbox

sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup ros-humble-turtlebot3*

sudo apt install ros-humble-twist-mux 

sudo apt install ros-humble-twist-stamper


----------Launch sim--------------
terminal 1: gazebo
ros2 launch rc_car launch_sim.launch.py world:=src/rc_car/worlds/obstacles.world
ros2 launch rc_car launch_sim.launch.py world:=src/rc_car/worlds/maze1.world


terminal 2: rviz
ros2 run rviz2 rviz2 -d src/rc_car/config/main.rviz --ros-args -p use_sim_time:=true


terminal 3: slam toolbox (mapping)
add map to rviz
ros2 launch rc_car online_async_launch.py use_sim_time:=true
save the map with rviz, add new panel->slam tool box plugin, serialize the map

reset the simulation, 
change the mapper params online async.yaml:

mode: localization
map_file_name: /home/ori/dev_ws/my_map_serial
map_start_at_dock: true


need to copy the localizion_launch from slam_toolbox and rerun the simulation
this is not the same localization_launch from Nav2 package(in this repo)
-----------------------------------------



--- gazebo + Rviz + localization + navigation -----
from this point we dont use slam_toolbox - so the base map will not get updates.

---terminal 1---:
ros2 launch rc_car launch_sim.launch.py world:=src/rc_car/worlds/maze1.world

---terminal 2---:
ros2 run rviz2 rviz2 -d src/rc_car/config/main.rviz --ros-args -p use_sim_time:=true

---terminal 3---:
ros2 launch rc_car localization_launch.py map:=./src/rc_car/maps/maze_1/maze1_map.yaml use_sim_time:=true

step 1: in rviz, manually write "map" in fixed frame
step 2: change set initial position
step 3: add map
step 4: topic->durability policy->transient local

---terminal 4---:
ros2 launch rc_car navigation_launch.py use_sim_time:=true map_subscribe_transient_local:=true

step 1:add map
step 2: topic: /global_costmap, color scheme: cost_map


-----------------------------------

REAL ROBOT

download imager to burn OS to PI
option 1: download ubuntu mate for PI 64 from https://ubuntu-mate.org/download/
option 2: https://ubuntu.com/download/raspberry-pi/thank-you?version=22.04.3&architecture=desktop-arm64+raspi 
burn the image to the micro-sd card

* CRITICAL*
after installtion update TIME and DATE before sudo apt update and upgrade

only for dev machine:
    sudo snap install --classic code

sudo apt install git 
install arduino: https://docs.arduino.cc/software/ide-v1/tutorials/Linux
if option 1 selected:
    only on pi: sudo apt remove brltty
    sudo nano /boot/firmware/config.txt 
            -> change: camera_auto_detect=0
            -> add new line: start_x=1

install ros:https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html
        -> skip: set locale
        -> setup sources
        -> install ros2 packages , desktop version

sudo apt-get install python3-pip
pip install setuptools==58.2.0

setting up ssh:
1. sudo apt install openssh-server
2. service ssh status
3. sudo ufw allow ssh
4. ssh 127.0.0.1
5. ip addr
6. ssh robot1@172.20.10.5


Low level
serial over usb:
sudo apt install python3-serial / sudo pip install pyserial
sudo apt install libserial-dev
sudo adduser $USER dialout


arduino ros bridge:
https://github.com/joshnewans/ros_arduino_bridge.git

add permission to arduino:
sudo chmod a+rw /dev/ttyACM0



run in terminal 
pyserial-miniterm -e /dev/ttyACM0 57600


how to remap:
ros2 run teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstampted


low level control packages:
1. ros_arduino_bridge - burn to arduino
pyserial-miniterm -e /dev/ttyACM0 57600
with o - open loop, e- encoders, m-closed loop

2. serial_motor_demo - gui to send commands over node - clone and colcon build

1.+2. works with topics, not as ros2_control 

diff_drive_arduino- hardware interface
diff_drive_arduino + serial works with ros2_control, the diffdrive_arduino package is called from ros2_control.xacro



------------ ROS BICYCLE SIMULATION ------------------

TERMINAL 1 :
ros2 launch rc_car launch_sim_bicycle.launch.py world:=src/rc_car/worlds/maze1.world

TERMINAL 2 :
ros2 run rviz2 rviz2 -d src/rc_car/config/main.rviz --ros-args -p use_sim_time:=true

TERMINAL 3 :
ros2 launch rc_car localization_launch.py map:=./src/rc_car/maps/maze_1/maze1_map.yaml use_sim_time:=true

step 1: in rviz, manually write "map" in fixed frame
step 2: change set initial position
step 3: add map
step 4: topic->durability policy->transient local

---terminal 4---:
ros2 launch rc_car navigation_launch.py use_sim_time:=true map_subscribe_transient_local:=true

step 1:add map
step 2: topic: /global_costmap, color scheme: cost_map



---------------------------
burn to arduino: https://github.com/joshnewans/ros_arduino_bridge.git

download to src file at the PI:
https://github.com/joshnewans/diffdrive_arduino/tree/humble
https://github.com/joshnewans/serial
