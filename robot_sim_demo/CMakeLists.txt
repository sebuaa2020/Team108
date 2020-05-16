cmake_minimum_required(VERSION 2.8.3)
project(robot_sim_demo)
find_package(catkin REQUIRED COMPONENTS
	roscpp
	rospy
	std_msgs
	message_generation
	controller_manager
	gazebo_ros
)

catkin_package(
   CATKIN_DEPENDS urdf xacro
)




include_directories(
  include ${catkin_INCLUDE_DIRS}
)

add_executable(keyboard_vel_ctrl
  src/keyboard_vel_ctrl.cpp
)
add_dependencies(keyboard_vel_ctrl ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(keyboard_vel_ctrl
  ${catkin_LIBRARIES}
)