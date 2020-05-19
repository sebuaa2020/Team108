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

4. 最后进行地图保存，地图默认保存地址在本地文件夹下，运行指令为：

   ```bash
   rosrun map_server map_saver -f map
   ```
  
   waterplus_map_tools/add_point.launch文件添加导航点
   wpb_home_tutorials/gmapping.launch文件用来建图
   wpb_home_apps/6_path_plan.launch文件用来多点导航

### 新增航点部分

主要涉及`add_waypoint.launch`和`wp_saver`两个文件，wpb_home_nav_test.launch用于测试

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

## 完成任务的整体文件

主要参见my_total文件夹内容，其中的.cpp文件搭建起了项目的整体框架





