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



## 避障与自由行走模块

这一部分主要写作于my_vel_package文件夹下的相关文件中，主要包括机器人进行基本建图操作时的自由行走、避障、路径重新规划等部分，
具体内容参见.launch文件和src文件夹

my_vel_package/src/vel_ctrl.cpp
主要分为3部分，前向障碍物检测、自由行走、自由行走中遇到障碍物时的路径规划是进行自由行走的代码吧，我看里面autonomous是总和了前面部分，如果运动时间达到上限会停止，如果没有遇到障碍物则按照给定speed直线进行，否则将会进行169次迭代查找周围哪些位置没有障碍物，一旦发现则调整新的转向，然后按照新的转向和速度前进？

## 完成任务的整体文件

主要参见my_total文件夹内容，其中的.cpp文件搭建起了项目的整体框架





