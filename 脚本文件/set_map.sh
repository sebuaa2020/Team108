#!/bin/bash
# This script is to run main controller to run other service


# cd catkin_ws
cd ../catkin_ws

# install dependencies
rosdep install --from-paths src --ignore-src --rosdistro=kinetic -y

# make ros
catkin_make

# source
source ./devel/setup.bash

# environment
export SVGA_VGPU10=0

# launch
roslaunch robot_sim_demo robot_spawn.launch
roslaunch wpb_home_tutorials gmapping.launch

# run
rosrun robot_sim_demo keyboard_vel_ctrl
rosrun map_server map_saver -f map
