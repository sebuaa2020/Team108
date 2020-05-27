#include "ros/ros.h"
#include <stdio.h>
#include <iostream>
#include <sensor_msgs/LaserScan.h>
#include <math.h>
#include <stdlib.h>
#include <cstdlib>


unsigned int num_readings = 360;
double laser_frequency = 10;
double ranges[num_readings];
sensor_msgs::LaserScan scan;

double x_region = 0.4,y_region = 0.25; 


void initialRanges(int i){
	int j;
	if(i==-1){ //没有障碍物 
		for(j=0;j<360;j++) ranges[j]=12.0;
	}
	else{ //有障碍物 
		for(j=0;j<360;j++){
			if(j==i) ranges[j]=0.25; 
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

void index(int i,int* startj,int* endj){
    if(i>=44) *startj = i-44;
    else *startj = i-44+360;

    if(i<315) *endj=i+45;
    else *endj=i+45-360;
}

bool find_path(sensor_msgs::LaserScan laser,int i)
{
    ROS_INFO("START FIND PATH");
    int j,startj,endj;
    double x,y;
    index(i,&startj,&endj);
    
    if(i<44){
        for(j=0;j<=endj;j++){
            if(isinf(laser.ranges[j])) continue;
            y = fabs(laser.ranges[j] * cos((j-i)*laser.angle_increment));
            x = fabs(laser.ranges[j] * sin((j-i)*laser.angle_increment));
            if ((x < x_region) && (fabs(y) < y_region)) return false;
        }
        for(j=startj;j<=359;j++){
	    if(isinf(laser.ranges[j])) continue;
            y = fabs(laser.ranges[j] * cos((j-i)*laser.angle_increment)); 
            x = fabs(laser.ranges[j] * sin((j-i)*laser.angle_increment));
            if ((x < x_region) && (fabs(y) < y_region)) return false;
        }
    }
    else if(i>=315){
        for(j=startj;j<=359;j++){
            if(isinf(laser.ranges[j])) continue;
            y = fabs(laser.ranges[j] * cos((j-i)*laser.angle_increment));            
            x = fabs(laser.ranges[j] * sin((j-i)*laser.angle_increment));
            if ((x < x_region) && (fabs(y) < y_region)) return false;
        }
        for(j=0;j<=endj;j++){
	    if(isinf(laser.ranges[j])) continue;
            y = fabs(laser.ranges[j] * cos((j-i)*laser.angle_increment));
            x = fabs(laser.ranges[j] * sin((j-i)*laser.angle_increment));
            if ((x < x_region) && (fabs(y) < y_region)) return false;
        }
    }
    else{
        for(j=startj;j<=endj;j++){
            if(isinf(laser.ranges[j])) continue;
            y = fabs(laser.ranges[j] * cos((j-i)*laser.angle_increment));
            x = fabs(laser.ranges[j] * sin((j-i)*laser.angle_increment));
            if ((x< x_region) && (fabs(y) < y_region)) return false;
        }
    }
    ROS_INFO("HAVE FOUND A PATH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
    return true;
}

void test(int i,int j){
	bool result;
	
	initialMsg(i);
	result=find_path(scan,j);
	
	if(i==-1) assert(result);
	else assert(!result);
}

int main(){
	ros::init(argc, argv, "test");
    ros::NodeHandle nh;
    
	test(-1,42);
	test(-1,315);
	test(-1,179);
	test(0,42);
	test(359,42);
	test(0,315);
	test(359,315)
	test(178,179);
	test(180,179);
	
	return 0;
}
