# sebuaa2020-Team108

![image-20200608161219878](img/readme_img.png)

### 项目结构

```
Team108:
  - code 		# 项目相关代码包及其使用简介、功能介绍
  - UI 			# 项目集成可视化界面
  - doc 		# 项目文档
  - scripts	 	# 添加项目运行用到的脚本文件
  - img			# 图片
  - 参考书籍			 # ros启智机器人开发参考书籍
  - 演示 				  # 相关演示视频
```

详细内容见[项目wiki](https://github.com/sebuaa2020/Team108/wiki/)

### 展示视频及代码PPT

[北航云盘展示视频链接](https://bhpan.buaa.edu.cn:443/link/1E63B997905FBF42A983C4A7570A9D80) 有效期限：2020-07-07 23:59

- 建立地图：演示通过GUI界面进行仿真环境的运行，以及视频机器人地图构建功能。
- 动态避障：演示在机器人规划好的路径上添加一个障碍物，机器人进行动态避障的功能。
- 定点巡航：演示机器人规划路径沿航点巡游的功能。
- 自由行走和避障：演示机器人按照指定时间、速度自由行走的功能。
- 语音建图：演示机器人根据语音输入进行反馈，通过语音控制来使机器人动态移动的功能。
- 代码展示：对代码实现进行详细介绍，与功能相对应。

### 运行环境

- Ubuntu 16.04
- ROS kinetic
- IAI-Kinect2
- python3.5
- PyQt5

### 使用步骤

1. 安装运行环境

   运行`setup.sh`文件安装ROS

2. 获取源码

   ```
   git clone https://github.com/sebuaa2020/Team108.git
   ```

3. 编译运行

   - 编译源码包

     ```
     cd code
     rosdep install --from-paths src --ignore-src --rosdistro=kinetic -y
     catkin_make
     source devel/setup.bash
     ```

   - 运行GUI界面

     ```
     cd UI
     python LeftTabWidget.py
     ```

### 项目简介

本项目为北京航空航天大学计算机学院2020年春季学期《软件工程》课程Team108开发项目。在课程组提供的仿真环境下开发一款定点巡航、动态避障、建立地图、随机行走、语音建图、自由行走等功能的简易机器人。

### 运行指令

#### 基本介绍

##### 运行虚拟环境

```
roslaunch robot_sim_demo robot_spawn.launch
```

##### 运行建图部分

```
roslaunch wpb_home_tutorials gmapping.launch
```

随后关闭，界面为黑色

##### 地图保存部分

```
rosrun map_server map_saver -f map
```

##### 添加航点部分

```
roslaunch waterplus_map_tools add_waypoint.launch
```

添加航点成功

##### 多点巡航部分

```
roslaunch wpb_home_apps 6_path_plan.launch
```

#### 具体运行包及介绍

本项目涉及十余个源码包，具体的介绍在`code`文件夹下各源码包的`readme`文件中。

### 参考文献

------

[1] 启智ROS机器人开发手册

[2] 启智ROS机器人

[3] ROS Robot Programming