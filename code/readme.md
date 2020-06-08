# ROS开发

本次项目采用课程组的demo1虚拟环境，运行指令为：

```bash
roslaunch robot_sim_demo robot_spawn.launch
```

出现场景为

![场景图](.\Image\场景图.png)

## 导航模块

### 建图部分

涉及代码部分为`rplidar_ros`和`wpb_home_tutorials`两部分，
`rplidar_ros`主要是雷达部分，
`wpb_home_tutorials`有关具体建图部分。

2. 利用启智机器人的gmapping建图功能进行地图构建，运行指令为：

   ```bash
   roslaunch wpb_home_tutorials gmapping.launch
   ```

   出现场景为

   ![建图](.\Image\建图.png)

3. 由于在虚拟环境中操作机器人，因此采取键盘操纵的形式，运行指令为：

   ```bash
   rosrun robot_sim_demo keyboard_vel_ctrl
   ```

4. 也可以采用语音操纵行走的形式，机器人每收到一条可识别的语音指令均会反馈消息“好的”。运行指令为：

   ```
   roslaunch xfyun_kinetic voice_cmd_wpb_home
   ```
  
   
   
5. 最后进行地图保存，地图默认保存地址在本地文件夹下，运行指令为：

   ```bash
   rosrun map_server map_saver -f map
   ```

   waterplus_map_tools/add_point.launch文件添加导航点
   wpb_home_tutorials/gmapping.launch文件用来建图
   wpb_home_apps/6_path_plan.launch文件用来多点导航

### 新增航点部分

主要涉及`add_waypoint.launch`和`wp_saver`两个文件，`wpb_home_nav_test.launch`用于测试

`add_waypoint.launch`用于新增航点

`wp——saver`将航点保存为waypoints.xml

`wp——saver`将航点保存为`waypoints.xml`

`wpb_home_nav_test.launch`测试航点是否能正常加载

1. 运行`add_waypoint.launch`文件添加航点，注意修改`add_waypoint.launch`中`load`的路径为想要保存的路径：

   ```bash
   roslaunch waterplus_map_tools add_waypoint.launch
   ```

2. 保持add_waypoint.launch的终端别关闭，将设置的航点保存在`waypoints.xml`中：

   ```bash
   rosrun waterplus_map_tools wp_saver
   ```

3. 修改`waypoint.xml`文件，第一个航点名设为`start`

4. 可以使用`wpb_home_nav_test.launch`测试航点是否能够正常加载，注意修改`wpb_home_nav_test.launch `中的load参数为`waypoints.xml`的路径：

   ```bash
   roslaunch waterplus_map_tools wpb_home_nav_test.launch
   ```

### 多点巡航部分

涉及的源码主要在`wpb_home_apps`包，其主要功能是新建航点，实现遍历所有航点的路径规划功能。具体内容详见`wpb_home_apps/src`文件夹下。

在多点巡航任务中，系统有如下四个状态

```
#define STATE_READY       0	// 准备状态
#define STATE_WAIT_ENTR   1	// 系统初始化，准备到达起点状态
#define STATE_GOTO        2	// 运行状态
#define STATE_DONE        3	// 任务完成状态
```

ros模块首先初始化5个待遍历航点。随后经过一系列初始化操作，开始系统的运行。

任务待开始时，系统的状态是`STATE_WAIT_ENTER`，然后当系统检测到有`entrance_detect`模块传进来的20条`door open`信息之后，出发至场地的起点。并更改状态为运行状态。

```cpp
 if(!ac.waitForServer(ros::Duration(5.0)))
{
	// 服务器请求失败
    ROS_INFO("The move_base action server is no running. action abort...");
}
else
{
    ...
    {
        ROS_INFO("Arrived at %s!",strGoto.c_str());
        //到达"start"航点,开始执行航点遍历脚本
        Speak("I am ready.");
        ros::spinOnce();
        sleep(3);
		// 更改状态为运行状态
        nState = STATE_GOTO; 
        strGoto = arWaypoint[nWaypointIndex];
        nWaypointIndex ++;
    }
    else
        ROS_INFO("Failed to get to %s ...",strGoto.c_str() );	// 到达目标地点失败
}
```

之后，机器人依次遍历之后的航点。直至遍历完成，更改状态为`STATE_DONE`，或者运行过程中产生异常重新执行其待到达的下一目标。

## 避障与自由行走模块

这一部分主要写作于my_vel_package文件夹下的相关文件中，主要包括机器人进行基本建图操作时的自由行走、避障、路径重新规划等部分，
具体内容参见.launch文件和src文件夹

my_vel_package/src/vel_ctrl.cpp
主要分为3部分，前向障碍物检测、自由行走、自由行走中遇到障碍物时的路径规划是进行自由行走的代码吧，我看里面autonomous是总和了前面部分，如果运动时间达到上限会停止，如果没有遇到障碍物则按照给定speed直线进行，否则将会进行169次迭代查找周围哪些位置没有障碍物，一旦发现则调整新的转向，然后按照新的转向和速度前进？

主要在`my_vel_package`包，其主要功能是实现机器人基本建图时的自由行走、自由行走中的避障，以及在遇到障碍物时更换方向继续做自由行走。
`my_vel_packag/src/vel_ctrl.cpp` 运动控制`Node`，实现对机器人运动的控制

1. 设置机器人自由行走的初始方向和速度
2. 如果运动时间达到上限会停止，如果没有，且没有遇到障碍物，则按照给定speed直线进行
3. 遇到障碍物，将会进行169次迭代，查找周围哪些位置没有障碍物，一旦发现则调整新的转向，然后按照新的转向和速度前进

代码的开始，先调用 `ros::init(argc, argv, "vel_ctrl")`;进行该节点的初始化操作，接下来声明一个` ros::NodeHandle` 对象 n，并用 n 生成一个广播对象 `vel_pub`，通过这个广播对象实现对机器人的控制（注意ROS约定机器人速度控制主题“/`md_vel`”）
为了连续不断的发送速度，使用一个 `while(ros::ok())`循环，以`ros::ok()`返回值作为循环结束条件可以让循环在程序关闭时正常退出。
为了发送速度值，声明一个 `geometry_msgs::Twist` 类型的对象 `vel_cmd`，并将速度值赋值到这个对象里。
vel_cmd 赋值完毕后，使用广播对象 vel_pub 将其发布到主题“/cmd_vel”上去。机器人的核心节点会从这个主题接收我们发过去的速度值，并转发到硬件机体去执行。

其中：
`vel_cmd.linear.x` 是机器人前后平移运动速度，正值往前，负值往后，单位是“米/秒”；
`vel_cmd.linear.y` 是机器人左右平移运动速度，正值往左，负值往右，单位是“米/秒”；
`vel_cmd.angular.z`（注意 angular）是机器人自转速度，正值左转，负值右转，单位是
“弧度/秒”；
其他值对启智机器人来说没有意义，所以都赋值为零。

1. 运行指令为：

   ```
   rosrun my_vel_package vel_ctrl
   ```

2. 此外，我们对官方源码进行部分修改，实现更为灵活的避障，运行指令为：

   ```
   rosrun wpb_home_tutorials wpb_home_behavior_node 
   ```

   


## 完成任务的整体文件

主要参见my_total文件夹内容，其中的.cpp文件搭建起了项目的整体框架
这部分代码在一定程度上参考了《开发手册》竞赛场景应用的一些思路和做法

主要在`my_total`包，其主要功能是搭建程序的主要框架，调动其他部分完成功能。
对应指令 
```
roslaunch wpb_home_apps shopping.launch
```

在这部分程序中实现了一个有限状态机，通过变量nState的赋值来表示机器人不同状态的衔接与跳转。

```STATE_READY    机器人调整完毕，准备接收下一步指令
STATE_FOLLOW    机器人开始使用激光雷达建图
STATE_ASK    机器人等待下一步指令
STATE_GOTO    机器人向给定导航点移动
STATE_GRAB    机器人进行抓取动作
STATE_COMBACK    机器人返回
STATE_PASS    机器人递交抓取到的物体
```
my_total/src/shopping.cpp中函数很多，其中：
主函数 int main()中，对变量的初始化和各种主题订阅、发布，
在while循环中具体实现有限状态机，在每种状态中根据条件完成状态跳转。
void AddNewWaypoint(string inStr)函数能将机器人在地图中的当前位置保存为航
点，参数为要保存的航点名称。



注：App_development 开发中的app端server代码 
