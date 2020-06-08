/*********************************************************************
* Software License Agreement (BSD License)
*
*  Copyright (c) 2017-2020, Waterplus http://www.6-robot.com
*  All rights reserved.
*
*  Redistribution and use in source and binary forms, with or without
*  modification, are permitted provided that the following conditions
*  are met:
*
*   * Redistributions of source code must retain the above copyright
*     notice, this list of conditions and the following disclaimer.
*   * Redistributions in binary form must reproduce the above
*     copyright notice, this list of conditions and the following
*     disclaimer in the documentation and/or other materials provided
*     with the distribution.
*   * Neither the name of the WaterPlus nor the names of its
*     contributors may be used to endorse or promote products derived
*     from this software without specific prior written permission.
*
*  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
*  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
*  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
*  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
*  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
*  FOOTPRINTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
*  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
*  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
*  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
*  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
*  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
*  POSSIBILITY OF SUCH DAMAGE.
*********************************************************************/
/*!******************************************************************
 @author     ZhangWanjie
 ********************************************************************/

#include <fstream>
#include <geometry_msgs/Twist.h>
#include <iostream>
#include <ros/ros.h>
#include <sensor_msgs/LaserScan.h>
#include <sstream>
#include <std_msgs/String.h>
#include <string>
#include <vector>
#include <stdio.h>
using namespace std;

ros::Publisher vel_pub;

template <class Type> Type stringToNum(const string &str) {
  istringstream iss(str);
  Type num;
  iss >> num;
  return num;
}

void lidarCallback(const sensor_msgs::LaserScan::ConstPtr &scan) {
  int nNum = scan->ranges.size();

  int nMid = nNum / 2;
  float fMidDist = scan->ranges[nMid];
  ROS_INFO("Point[%d] = %f", nMid, fMidDist);

  geometry_msgs::Twist vel_cmd;
  if (fMidDist > 1.0f) {
    vel_cmd.linear.x = 0.3;
  } else {
    vel_cmd.angular.z = 5;
  }
  vel_pub.publish(vel_cmd);
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "wpb_home_behavior_node");
    string s;
    ifstream fp("config.txt");
    if (fp) {
      cout << "file error";
      exit(1);
    }
    int i = 0;
    while (getline(fp, s)) {
      if (i == 0) {
        ROS_INFO("the speed is %s : ", s);
        i = i + 1;
      } else {
        ROS_INFO("the time is %s : ", s);
      }
    }

    fp.close();
    // ifstream file;
    // file.open("config.txt");
    // if (!file.is_open()) {
    //   cout << "ERROR with file";
    //   exit(1);
    // }
    char buffer[32];
    // int i = 0;
    double desttime, newspeed;
  //   while (!file.eof()) {
  //     file.getline(buffer, 32);
  //     if (i == 0) {
  //       newspeed = atoi(buffer);
  //       ROS_INFO("%lf", newspeed);
  //       i++;
  //     } else {
  //       desttime = atoi(buffer);
  //       ROS_INFO("%lf", desttime);
  //     }
  //   }
//   FILE *fp;
//   if ((fp = fopen("config.txt",
//                   "r")) == NULL) {
//     cout << "file error";
//     exit(1);
//   }
//   while (fgets(buffer, 32, fp) != NULL) {
//     if (i == 0) {
//       newspeed = atoi(buffer);
//       i++;
//     } else
//       desttime = atoi(buffer);
//   }
  ROS_INFO("wpb_home_behavior_node start!");

  ros::NodeHandle nh;
  ros::Subscriber lidar_sub = nh.subscribe("/scan", 10, &lidarCallback);
  vel_pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel", 10);

  ros::spin();
}