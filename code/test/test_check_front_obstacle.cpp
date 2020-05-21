#include "ros/ros.h"
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <cstdlib>
#include <assert.h>
#include <sensor_msgs/LaserScan.h>

unsigned int num_readings = 360;
double laser_frequency = 10;
double ranges[num_readings];
sensor_msgs::LaserScan scan;

int start_index = 134 ,end_index = 225;
double x_region = 0.4,y_region = 0.25;

void initialRanges(int i){
	int j;
	if(i==0){ //没有障碍物 
		for(j=0;j<360;j++) ranges[j]=12.0;
	}
	else{ //有障碍物 
		for(j=0;j<360;j++){
			if(j==178) ranges[j]=0.25; 
			else ranges[j]=12.0;
		}
	}
}

void initialMsg(int j){
	ros::Time scan_time = ros::Time::now();
	
	initialRanges(j);
    scan.header.stamp = scan_time;
    scan.header.frame_id = "base_link";
    scan.angle_min = -3.14;
    scan.angle_max = 3.14;
    scan.angle_increment = 3.14 / num_readings;
    scan.time_increment = (1 / laser_frequency) / (num_readings);
    scan.range_min = 0.15;
    scan.range_max = 12.0;
    scan.ranges.resize(num_readings);
    
    for(unsigned int i = 0; i < num_readings; ++i){
        scan.ranges[i] = ranges[i];
    }
}

void test(int i){
	bool result;
	
	initialMsg(i);
	result=check_front_obstacle(scan);
	
	if(i==0) assert(!result);
	else assert(result);
}

bool check_front_obstacle(sensor_msgs::LaserScan laser)
{
	for(int i=start_index; i<end_index; i++)
	{
		double x,y;
        if(!isinf(laser.ranges[i])){	
			y = laser.ranges[i] * sin(laser.angle_min + i * laser.angle_increment);
        	x = laser.ranges[i] * cos(laser.angle_min + i * laser.angle_increment);
		}
		else continue;
        if (( x < x_region) && (fabs(y) < y_region)) {
			ROS_INFO("CHECK FRONT OBSTACLES TRUE");			
			return true;
		}
	}
	return false;
}



int main(int argc, char **argv)
{
    ros::init(argc, argv, "test");
    ros::NodeHandle nh;
    
    test(0); //测试没有障碍物 
    test(1); //测试有障碍物 

    return 0;
}
