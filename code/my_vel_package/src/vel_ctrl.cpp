#include "ros/ros.h"
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <geometry_msgs/Twist.h>
#include <std_msgs/Int8.h>
#include <sensor_msgs/LaserScan.h>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include "exception.h"

#define RAYS 1081
#define PI 3.1415
#define STEP 10

using namespace std;

int start_index = 134, end_index = 225;
double newturnrate = 0, x_region = 0.4, y_region = 0.25, start, t, desttime, newspeed;
float speed = 0.08;


geometry_msgs::Twist cmd_vel;
ros::Publisher cmd_vel_pub;
ros::Publisher cmd_stop_pub;
std_msgs::Int8 stop_vel;

// æ£€æµ‹å‰æ–¹éšœç¢ç‰©
bool check_front_obstacle(sensor_msgs::LaserScan laser) {
	for(int i = start_index; i < end_index; i++) {
		double x,y;
        if(!isinf(laser.ranges[i])) {
			y = laser.ranges[i] * sin(laser.angle_min + i * laser.angle_increment);
            x = laser.ranges[i] * cos(laser.angle_min + i * laser.angle_increment);
		} else {
            inf_error();
        }
        if (( x < x_region) && (fabs(y) < y_region)) {
			ROS_INFO("CHECK FRONT OBSTACLES TRUE");			
			return true;
		}
	}
	return false;
}

void index(int i,int* startj,int* endj){
    if(i >= 44) {
        *startj = i - 44;
    }
    else {
        *startj = i - 44 + 360;
    }

    if(i < 315) {
        *endj = i + 45;
    }
    else {
        *endj = i + 45 - 360;
    }
}


bool find_path(sensor_msgs::LaserScan laser,int i) {
    ROS_INFO("START FIND PATH");
    int j,startj,endj;
    double x,y;
    index(i, &startj, &endj);
    
    if(i < 44){
        for(j = 0; j <= endj; j++){
            if(isinf(laser.ranges[j])) {
                continue;
            }
            y = fabs(laser.ranges[j] * cos((j-i)*laser.angle_increment));
            x = fabs(laser.ranges[j] * sin((j-i)*laser.angle_increment));
            if ((x < x_region) && (fabs(y) < y_region)) {
                return false;
            }
        }
        for(j = startj; j <= 359; j++){
            if(isinf(laser.ranges[j])) {
                continue;
            }
            y = fabs(laser.ranges[j] * cos((j-i)*laser.angle_increment)); 
            x = fabs(laser.ranges[j] * sin((j-i)*laser.angle_increment));
            if ((x < x_region) && (fabs(y) < y_region)) {
                return false;
            }
        }
    }
    else if(i >= 315){
        for(j = startj; j <= 359; j++){
            if(isinf(laser.ranges[j])) {
                continue;
            }
            y = fabs(laser.ranges[j] * cos((j-i)*laser.angle_increment));
            x = fabs(laser.ranges[j] * sin((j-i)*laser.angle_increment));
            if ((x < x_region) && (fabs(y) < y_region)) {
                return false;
            }
        }
        for(j = 0; j <= endj; j++){
            if(isinf(laser.ranges[j])) {
                continue;
            }
            y = fabs(laser.ranges[j] * cos((j-i)*laser.angle_increment));
            x = fabs(laser.ranges[j] * sin((j-i)*laser.angle_increment));
            if ((x < x_region) && (fabs(y) < y_region)) {
                return false;
            }
        }
    }
    else{
        for(j = startj; j <= endj; j++){
            if(isinf(laser.ranges[j])) {
                continue;
            }
            y = fabs(laser.ranges[j] * cos((j-i)*laser.angle_increment));
            x = fabs(laser.ranges[j] * sin((j-i)*laser.angle_increment));
            if ((x< x_region) && (fabs(y) < y_region)) {
                return false;
            }
        }
    }
    ROS_INFO("HAVE FOUND A PATH!");
    return true;
}

// æœºå™¨äººæ§åˆ¶
void autonomous_behave(const sensor_msgs::LaserScan &laser) {
    newspeed = newturnrate = 0.0; 
    bool result;
    int i, num, j = 0;
    double end;

    end=ros::Time::now().toSec();
    ROS_INFO("%d\n",end-start);
    
    if(end - start >= desttime){
        while(j <= 4) {
            // æœºå™¨äººå‰åå¹³ç§»é€Ÿåº¦ m/s
            cmd_vel.linear.x = 0.0;
            // æœºå™¨äººå·¦å³å¹³ç§»é€Ÿåº¦ m/s
    	    cmd_vel.linear.y = 0.0;
            // æ— æ„ä¹‰
    	    cmd_vel.linear.z = 0.0;
            // æ— æ„ä¹‰
    	    cmd_vel.angular.x = 0.0;
            // æ— æ„ä¹‰
    	    cmd_vel.angular.y = 0.0;
            // æœºå™¨äººè‡ªè½¬é€Ÿåº¦ å¼§åº¦/s
    	    cmd_vel.angular.z = 0.0;
            // èµ‹å€¼å®Œæ¯•ï¼Œä½¿ç”¨å¹¿æ’­å¯¹è±¡cmd_velå‘å¸ƒåˆ°ä¸»é¢˜/cmd_vel â€”â€” æœºå™¨äººé€Ÿåº¦æ§åˆ¶ä¸»é¢˜ ä¸Šå»
            cmd_vel_pub.publish(cmd_vel);
            j++;
        }
        ros::shutdown();
    }
    /*
    ÆäÖĞ£º
    vel_cmd.linear.x ÊÇ»úÆ÷ÈËÇ°ºóÆ½ÒÆÔË¶¯ËÙ¶È£¬ÕıÖµÍùÇ°£¬¸ºÖµÍùºó£¬µ¥Î»ÊÇ¡°Ã×/Ãë¡±£»
    vel_cmd.linear.y ÊÇ»úÆ÷ÈË×óÓÒÆ½ÒÆÔË¶¯ËÙ¶È£¬ÕıÖµÍù×ó£¬¸ºÖµÍùÓÒ£¬µ¥Î»ÊÇ¡°Ã×/Ãë¡±£»
    vel_cmd.angular.z£¨×¢Òâ angular£©ÊÇ»úÆ÷ÈË×Ô×ªËÙ¶È£¬ÕıÖµ×ó×ª£¬¸ºÖµÓÒ×ª£¬µ¥Î»ÊÇ
    ¡°»¡¶È/Ãë¡±£»
    ÆäËûÖµ¶ÔÆôÖÇ»úÆ÷ÈËÀ´ËµÃ»ÓĞÒâÒå£¬ËùÒÔ¶¼¸³ÖµÎªÁã¡£    
    */ 

    // è‡ªç”±è¡Œèµ°è¿‡ç¨‹ä¸­ æ²¡æœ‰é‡åˆ°éšœç¢ç‰© åˆ™æŒ‰ç»™å®šspeedç›´çº¿è¿åŠ¨
    if(!check_front_obstacle(laser)) {
    	cmd_vel.linear.x = speed;
    	cmd_vel.linear.y = 0.0;
    	cmd_vel.linear.z = 0.0;
    	cmd_vel.angular.x = 0.0;
    	cmd_vel.angular.y = 0.0;
    	cmd_vel.angular.z = 0.0;
    	cmd_vel_pub.publish(cmd_vel);
        return;
    }

    // é‡åˆ°éšœç¢ç‰©å è¿›è¡Œ169æ¬¡è¿­ä»£æŸ¥æ‰¾å‘¨å›´å“ªäº›ä½ç½®æ²¡æœ‰éšœç¢ç‰©
    for(i = 169; i >= 0; i = i - STEP) {
        result = find_path(laser, i);
        if(result == true) {
            break;
        }
    }
    
    if(result == false) {
        for(i = 189; i <= 359; i = i + STEP) {
            result = find_path(laser, i);
            if(result==true) {
                break;
            }
        }
    }
   
    if(result == true) {
        ROS_INFO("WE HAVE FIND IT hhh!");
        if(i <= 178 && i >= 0){
            newturnrate = -PI/10;
            t = fabs((179-i)*laser.angle_increment/newturnrate);
        } else{
            newturnrate = PI/10;
            t = fabs((i-179)*laser.angle_increment/newturnrate);
        }
    } else {
        ROS_INFO("LZZ is so lovely!");
    }
    cmd_vel.linear.x = newspeed;
    cmd_vel.linear.y = 0.0;
    cmd_vel.linear.z = 0.0;
    cmd_vel.angular.x = 0.0;
    cmd_vel.angular.y = 0.0;
    cmd_vel.angular.z = newturnrate;
    cmd_vel_pub.publish(cmd_vel);
    ROS_INFO("t = %f, newturnrate = %lf, i = %d", t, newturnrate, i);
    ros::Duration(t).sleep();
}


int main(int argc, char **argv) {
    // è¿›è¡ŒèŠ‚ç‚¹çš„åˆå§‹åŒ–æ“ä½œï¼Œç¬¬3ä¸ªå‚æ•°ä¸ºèŠ‚ç‚¹åç§°
    ros::init(argc, argv, "laser_obstacle_avoidance");
    ros::NodeHandle nh;
    char buffer[32];
    int i=0;
   /*
    ifstream file;
    file.open("config",ios::in);
    if(!file.is_open()){ 
        cout<<"ERROR with file";
        exit(1);
    }
    while(!file.eof()){
        file.getline(buffer,32);
        if(i==0){
	    newspeed=atoi(buffer);
	    ROS_INFO("%lf",newspeed);
	    i++;
	}
	else{
	    desttime=atoi(buffer);
	    ROS_INFO("%lf",desttime);
        }
    }*/
	
    FILE *fp;
    if((fp= fopen("/home/robot/catkin_ws/src/my_vel_package/src/config.txt","r"))==NULL) {
        file_no_open();
        exit(1);
    }
    while(fgets(buffer,32,fp) != NULL) {
        if(i == 0){
            newspeed = atoi(buffer);
            i++;
        } else {
            desttime = atoi(buffer);
        }
    }
    
    cmd_vel_pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel", 1);
    ros::Subscriber laser_sub = nh.subscribe("/scan", 1, autonomous_behave);
    start=ros::Time::now().toSec();
    
    ros::spin();
    return 0;
}
