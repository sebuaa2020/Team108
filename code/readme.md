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
   
 ### 新增航点部分

主要涉及`add_waypoint.launch`和`wp_saver`两个文件，wpb_home_nav_test.launch用于测试
`add_waypoint.launch`用于新增航点，
`wp——saver`将航点保存为waypoints.xml
`wpb_home_nav_test.launch`测试航点是否能正常加载

1. 运行add_waypoint.launch文件添加航点，注意修改add_waypoint.launch中load的路径为想要保存的路径：

   ```bash
   roslaunch waterplus_map_tools add_waypoint.launch
   ```
   
2. 保持add_waypoint.launch的终端别关闭，将设置的航点保存在waypoints.xml中：

   ```bash
   rosrun waterplus_map_tools wp_saver
   ```
   
3.修改waypoint.xml文件，第一个航点名设为start

4. 可以使用wpb_home_nav_test.launch测试航点是否能够正常加载，注意修改wpb_home_nav_test.launch 中的load参数为waypoints.xml的路径：

   ```bash
   roslaunch waterplus_map_tools wpb_home_nav_test.launch
   ```
   
   waterplus_map_tools/add_point.launch文件添加导航点
   wpb_home_tutorials/gmapping.launch文件用来建图
   wpb_home_apps/6_path_plan.launch文件用来多点导航



## 避障与自由行走模块

这一部分主要写作于my_vel_package文件夹下的相关文件中，主要包括机器人进行基本建图操作时的自由行走、避障、路径重新规划等部分，
具体内容参见.launch文件和src文件夹

## 完成任务的整体文件

主要参见my_total文件夹内容，其中的.cpp文件搭建起了项目的整体框架





