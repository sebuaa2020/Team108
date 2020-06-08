#!/bin/bash

if ! [ -d "/opt/ros/kinetic" ]; then
  echo "install ros-kinetic"

  # install ros kinetic
  sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
  sudo apt-get update
  sudo apt-get install ros-kinetic-desktop-full

  # environment setup
  echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc

  # install dependencies
  sudo apt-get install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
  sudo apt-get install python-rosdep
  sudo rosdep init
  rosdep update
fi

echo "ros setup finished!"