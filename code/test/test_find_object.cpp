#include <iostream>
#include <ros/ros.h>
#include <std_msgs/String.h>
#include <geometry_msgs/Twist.h>
#include <sound_play/SoundRequest.h>
#include <sensor_msgs/Image.h> 
#include <string>
#include <darknet_ros_msgs/BoundingBoxes.h>
#include <darknet_ros_msgs/BoundingBox.h>
#include <darknet_ros_msgs/CheckForObjectsAction.h>

#define OBJ "bottle"
#define OBJ1 "cup"
#define OBJ2 "bottle"
#define OBJ3 "laptop"

static darknet_ros_msgs::BoundingBoxes msg;

void MyCB(const darknet_ros_msgs::BoundingBoxes &msg) {
	int i, size, index1 = -1, index2 = -1, index3 = -1, xmin, minindex, temp, index_obj = -1, cnt = 0;
	ROS_WARN("CALLBACKHERE");
	if(flag == 0) {
		ROS_WARN("enter flag");
		size = msg.num;
		ROS_WARN("size = %d",size);
		darknet_ros_msgs::BoundingBox object_array[3];
		
		for(i = 0; i < size; i++) {
            if(msg.bounding_boxes[i].Class.compare(OBJ)==0) {
                index_obj = i;
            }
            if(msg.bounding_boxes[i].Class.compare(OBJ1)==0) {
                index1 = i;
            }
            else if(msg.bounding_boxes[i].Class.compare(OBJ2)==0) {
                index2 = i;
            }
            else if(msg.bounding_boxes[i].Class.compare(OBJ3)==0) {
                index3 = i;
            }
			cout << msg.bounding_boxes[i].Class << endl;
		}
		ROS_WARN("comparison completed");
		if(index1 >= 0 && index2 >= 0 && index3 >= 0 && index_obj >= 0) {
			ROS_WARN("three required object detected!");
			object_array[0] = msg.bounding_boxes[index1];
			object_array[1] = msg.bounding_boxes[index2];
			object_array[2] = msg.bounding_boxes[index3];
			cnt = 0;
			xmin = msg.bounding_boxes[index_obj].xmin;
			for(i=0; i<size; i++){
                if(object_array[i].xmin<xmin) {
                    cnt++;
                }
			}	
			ROS_WARN("cnt = %d", cnt)
			ROS_WARN("change state to STATE_GOTO");
			strGoto = index2waypoint[cnt];
			nState = STATE_GOTO;
			flag++;
		}
		ROS_WARN("END");
	}
}

void change_msg(int object_num,String Class[],int xmin[]) {
    //实际上用到的属性只有这三个，所以就只需要改变这三个参数
	msg.num = num;
	int i = 0;
	for(i = 0; i < num; i++) {
		msg.bounding_boxes[i].Class = Class[i];
		msg.bounding_boxes[i].xmin = xmin[i];
	}
}

int main(){
	change_msg(2, {"cup", "bottle"}, {700, 800});
	MyCB(msg);
	
	change_msg(3, {"bottle", "cup", "laptop"}, {100, 200, 300});
	MyCB(msg);
	
	change_msg(5, {"bottle", "cup", "laptop", "bottle", "bottle"}, {400, 500, 600, 700, 800});
	MyCB(msg);
	
	change_msg(4, {"mouse", "person", "laptop", "cell phone"}, {700, 800, 900, 1000});
	MyCB(msg);
}
