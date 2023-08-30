# Autonomous_RC


first install ros2 humble - see documentation 

sudo apt install ros-humble-xacro ros-humble-joint-state-publisher-gui

git clone -b humble https://github.com/joshnewans/rc_car.git

sudo apt install ros-humble-rplidar-ros

ros2 ros2_control list_hardware_interfaces


sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-gazebo-ros2-control

git clone -b humble https://github.com/ros-controls/gazebo_ros2_control

sudo apt install joystick jstest-gtk evtest 

sudo apt install ros-humble-slam-toolbox

sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup ros-humble-turtlebot3*

sudo apt install ros-humble-twist-mux


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

---------------
run gazebo and rviz
this loads the saved map and localiztion
ros2 launch rc_car localization_launch.py use_sim_time:=true map:=./maze1_map.yaml 



--- add map to rviz -----

terminal 4: nav2 stack
ros2 launch rc_car navigation_launch.py use_sim_time:=true

