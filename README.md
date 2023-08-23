# Autonomous_RC


first install ros2, 

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

terminal 2: rviz
ros2 run rviz2 rviz2 -d src/rc_car/config/main.rviz --ros-args -p use_sim_time:=true

terminal 3: slam toolbox (mapping)
ros2 launch rc_car online_async_launch.py use_sim_time:=true
add map to rviz

terminal 4: nav2 stack
ros2 launch rc_car navigation_launch.py use_sim_time:=true# my_ackermann
