cmake_minimum_required(VERSION 3.5)
project(rc_car)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(interfaces REQUIRED)

# add_executable(mocap_node rc_car/print_mocap.py)
# ament_target_dependencies(rclpy geometry_msgs mocap_msgs)


# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_python_install_package(${PROJECT_NAME})


install(
  DIRECTORY config description launch scripts rviz_config
  DESTINATION share/${PROJECT_NAME}
)

# Install Python executables
install(PROGRAMS
  scripts/py_PRM.py
  scripts/ros_odom_publisher_bicycle.py
  scripts/ros_PID_wall_following.py
  scripts/ros_follow_the_gap.py
  scripts/ros_joy_to_cmdvel.py
  scripts/ros_Get_map_client.py
  scripts/ros_PathPlanning_service_astar.py
  scripts/ros_PathPlanning_service_prm.py
  scripts/ros_steering_calibration.py
  scripts/ros_optitrack_map_to_odom_publisher.py
  scripts/ros_PathPlanning_client.py
  scripts/ros_Path_Tracking.py
  scripts/py_PurePursuit.py
  scripts/py_Utils.py
  scripts/py_car_consts.py
  scripts/py_AStar.py
  scripts/ros_print_mocap.py
  DESTINATION lib/${PROJECT_NAME}
)


ament_package()
