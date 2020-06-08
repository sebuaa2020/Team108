#include <geometry_msgs/Twist.h>
#include <ros/ros.h>
#include <std_msgs/String.h>

#define CMD_STOP 0
#define CMD_FORWARD 1
#define CMD_BACKWARD 2
#define CMD_LEFT 3
#define CMD_RIGHT 4

#define CMD_DURATION 1

static ros::Publisher vel_pub;
static ros::Publisher spk_pub;
static int nCmd = CMD_STOP;
static int nCount = 0;

void KeywordCB(const std_msgs::String::ConstPtr &msg) {
//   ROS_WARN("[KeywordCB] - %s", msg->data);

  bool bCmd = false;
  int nFindIndex = 0;
  nFindIndex = msg->data.find("前");
  if (nFindIndex >= 0) {
    ROS_WARN("[KeywordCB] - move x");
    bCmd = true;
    nCmd = CMD_FORWARD;
  }
  nFindIndex = msg->data.find("后");
  if (nFindIndex >= 0) {
    ROS_WARN("[KeywordCB] - move -x");
    bCmd = true;
    nCmd = CMD_BACKWARD;
  }
  nFindIndex = msg->data.find("左");
  if (nFindIndex >= 0) {
    ROS_WARN("[KeywordCB] - move y");
    bCmd = true;
    nCmd = CMD_LEFT;
  }

  nFindIndex = msg->data.find("右");
  if (nFindIndex >= 0) {
    ROS_WARN("[KeywordCB] - move -y");
    bCmd = true;
    nCmd = CMD_RIGHT;
  }

  nFindIndex = msg->data.find("停");
  if (nFindIndex >= 0) {
    ROS_WARN("[KeywordCB] - stop");
    bCmd = true;
    nCmd = CMD_STOP;
  }

  std_msgs::String strSpeak;
  if (bCmd == true) {
    nCount = CMD_DURATION;
    strSpeak.data = "好的";
    spk_pub.publish(strSpeak);
  } else {
    // strSpeak = *msg;
  }
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "wp_voice_cmd_cn");

  ros::NodeHandle n;
  ros::Subscriber sub_sr = n.subscribe("/xfyun/iat", 10, KeywordCB);
  spk_pub = n.advertise<std_msgs::String>("/xfyun/tts", 20);
  vel_pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 10);
  geometry_msgs::Twist vel_cmd;
  vel_cmd.linear.x = 0;
  vel_cmd.linear.y = 0;
  vel_cmd.angular.z = 0;
  ros::Rate r(10);
  while (ros::ok()) {

    if (nCount > 0) {
      nCount--;
      if (nCmd == CMD_FORWARD) {
        if (vel_cmd.linear.x < 0.3) {
          vel_cmd.linear.x += 0.1;
        }
        // ROS_WARN("forward");
        printf("forward: linear.x= %.2f linear.y= %.2f angular.z= %.2f \n",
               vel_cmd.linear.x, vel_cmd.linear.y, vel_cmd.angular.z);
      }
      if (nCmd == CMD_BACKWARD) {
        if (vel_cmd.linear.x > -0.3) {
          vel_cmd.linear.x -= 0.1;
        }
        // vel_cmd.linear.x = -0.1;
        // ROS_WARN("backward");
        printf("backward: linear.x= %.2f linear.y= %.2f angular.z= %.2f \n",
               vel_cmd.linear.x, vel_cmd.linear.y, vel_cmd.angular.z);
      }
      if (nCmd == CMD_LEFT) {
        if (vel_cmd.linear.z < 0.3) {
          vel_cmd.angular.z += 0.1;
        }
        // vel_cmd.angular.z = 0.1;
        // ROS_WARN("left");
        printf("left: linear.x= %.2f linear.y= %.2f angular.z= %.2f \n",
               vel_cmd.linear.x, vel_cmd.linear.y, vel_cmd.angular.z);
      }
      if (nCmd == CMD_RIGHT) {
        if (vel_cmd.linear.z > -0.3) {
          vel_cmd.angular.z -= 0.1;
        }
        // vel_cmd.angular.z = -0.1;
        // ROS_WARN("right");
        printf("right: linear.x= %.2f linear.y= %.2f angular.z= %.2f \n",
               vel_cmd.linear.x, vel_cmd.linear.y, vel_cmd.angular.z);
      }
      if (nCmd == CMD_STOP) {
        vel_cmd.linear.x = 0;
        vel_cmd.linear.y = 0;
        vel_cmd.angular.z = 0;
        // ROS_WARN("stop");
        printf("stop: linear.x= %.2f linear.y= %.2f angular.z= %.2f \n",
               vel_cmd.linear.x, vel_cmd.linear.y, vel_cmd.angular.z);
      }
    } else {
      //   nCmd = CMD_STOP;
      //   vel_cmd.linear.x = 0;
      //   vel_cmd.linear.y = 0;
      //   vel_cmd.angular.z = 0;
      //   ROS_WARN("stop");
      printf("continue: linear.x= %.2f linear.y= %.2f angular.z= %.2f \n",
             vel_cmd.linear.x, vel_cmd.linear.y, vel_cmd.angular.z);
    }
    vel_pub.publish(vel_cmd);
    ros::spinOnce();
    r.sleep();
  }

  return 0;
}