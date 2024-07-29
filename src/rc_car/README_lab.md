# Autonomous Car
* CRITICAL*
after installtion update TIME and DATE before sudo apt update and upgrade

# building:
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source /opt/ros/humble/setup.bash
colocon build --symlink-install
source install/setup.bash


how to stop the lidar?
ros2 launch rc_car rplidar.launch.py 
ros2 service call /stop_motor std_srvs/srv/Empty "{}"
ros2 service call /start_motor std_srvs/srv/Empty "{}"


# --------------------- Real Robot --------------------

ssh robot1@192.168.0.102
cd car_hardware
source /opt/ros/humble/setup.bash
source install/setup.bash

ros2 launch rc_car launch_robot.launch.py
ros2 launch rc_car rplidar_s2.launch.py 

Rviz:
Rviz runs on remote computer and *NOT* via ssh!
ros2 run rviz2 rviz2 -d src/rc_car/rviz_config/localization.rviz --ros-args -p use_sim_time:=false

mapping:
ros2 launch rc_car online_async_launch.py use_sim_time:=false
1. panels -> add new panel -> slam tool box plugin
2. in rviz add map and set /map to topic, change durability policy TransientLocal
2. save the map with rviz, serialize the map

to store map as numpy array:
restart
run with localization and to save the map:
ros2 run rc_car ros_Get_map_client.py --ros-args -p map_name:=lab307


localiztion:
source install/setup.bash
ros2 launch rc_car localization.launch.py map:=race4.yaml use_sim_time:=false
1. in rviz, manually write "map" in fixed frame
2. change set initial position
3. add map
4. topic->durability policy->transient local
<!-- ros2 launch rc_car localization_launch.py map:=my_lab3.yaml use_sim_time:=false -->


navigation:
# path planning
ros2 run rc_car PathPlanning_service_prm.py --ros-args -p map_name:=map_world -p use_sime_time:=false
ros2 run rc_car PathPlanning_client.py 0 0 6.22 -4.5 path1  --ros-args -p use_sime_time:=false
# path tracking
NOTE - the path_name without the '_meter'
ros2 run rc_car ros_Path_Tracking.py --ros-args -p use_sime_time:=false -p show_path:=true -p show_marker:=true -p path_name:=path1


# ---------- General Notes ---------------------

REAL ROBOT NOTES
download imager to burn OS to PI
download ubuntu mate for PI 64 from https://ubuntu-mate.org/download/
install ros:https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html
        -> skip: set locale
        -> setup sources
        -> install ros2 packages , desktop version




ssh robot1@192.168.0.102
cd car_hardware
source /opt/ros/humble/setup.bash
source install/setup.bash





