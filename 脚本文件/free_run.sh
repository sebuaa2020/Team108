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
rosrun wpb_home_tutorials wpb_home_behavior_node