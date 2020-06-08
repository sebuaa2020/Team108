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
roslaunch waterplus_map_tools add_waypoint.launch
roslaunch wpb_home_apps 6_path_plan.launch