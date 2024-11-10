cmake_minimum_required(VERSION 3.5)
project(ur_robot_driver)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(ur_description REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(controller_manager REQUIRED)

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
