cmake_minimum_required(VERSION 3.5)
project(assembly_1_robot_arm)

# Find required packages
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED) # If you have Python scripts
find_package(rclpy REQUIRED)              # If you use Python nodes
find_package(robot_state_publisher REQUIRED)
find_package(joint_state_publisher_gui QUIET)
if(joint_state_publisher_gui_FOUND)
  message(STATUS "Found joint_state_publisher_gui")
else()
  message(WARNING "joint_state_publisher_gui not found. Ensure it is installed if needed.")
endif()

# Install directories
install(DIRECTORY
  launch
  urdf
  meshes
  config
  DESTINATION share/${PROJECT_NAME}
)

# If you have Python scripts, install them
# install(PROGRAMS
#   scripts/some_script.py
#   DESTINATION lib/${PROJECT_NAME}
# )

# Mark the package for ament
ament_package()

