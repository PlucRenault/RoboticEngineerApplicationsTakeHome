cmake_minimum_required(VERSION 3.5)
project(ur_description)

find_package(ament_cmake REQUIRED)
find_package(xacro REQUIRED)
find_package(urdf REQUIRED)

install(DIRECTORY urdf launch
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
