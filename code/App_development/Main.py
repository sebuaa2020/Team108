import socket
import threading
import os
import time
import subprocess


def str2shell(str):
    if str == 'map_start':
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_bringup minimal.launch; exec bash\"'")
        time.sleep(2)
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_tutorials hector_mapping.launch; exec bash\"'")
    if str == 'map_finish':
        os.system("gnome-terminal -e 'bash -c \"rosrun map_server map_saver -f map\"'")
        os.system("gnome-terminal -e 'bash -c \"cp ~/map.pgm ~/catkin_ws/src/team_108/maps/\"'")
        os.system("gnome-terminal -e 'bash -c \"cp ~/map.yaml ~/catkin_ws/src/team_108/maps/\"'")
        # reverseIns(action_list)
    if str == 'move_forward':
        os.system("gnome-terminal -e 'bash -c \"rosrun team_108 go_forward\"'")
    if str == 'move_backward':
        os.system("gnome-terminal -e 'bash -c \"rosrun team_108 go_backward\"'")
    if str == 'move_left':
        os.system("gnome-terminal -e 'bash -c \"rosrun team_108 go_left\"'")
    if str == 'move_right':
        os.system("gnome-terminal -e 'bash -c \"rosrun team_108 go_right\"'")
    if 'addNewWayPoint' in str:
        os.system("gnome-terminal -e 'bash -c \"roslaunch team_108 script_exc.launch\"'")
    if 'goto' in str:
        command = "gnome-terminal -e 'bash -c \"roslaunch team_108 script_goto"+str[4]+".launch\"'"
        os.system(command)

def str2shell2(str):
    global p_move, p_map , p_grab, p_navi
    if str == 'map_start':
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_bringup minimal.launch; exec bash\"'")
        time.sleep(2)
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_tutorials hector_mapping.launch; exec bash\"'")

    if str == 'map_finish':
        p_temp = subprocess.Popen('rosrun map_server map_saver -f map',shell=True)
        p_temp.wait()
        p_temp = subprocess.Popen('cp ~/map.pgm ~/catkin_ws/src/team_108/maps/', shell=True)
        p_temp.wait()
        p_temp = subprocess.Popen('cp ~/map.yaml ~/catkin_ws/src/team_108/maps/', shell=True)
        p_temp.wait()
        p_temp = subprocess.Popen('cp ~/map.pgm ~/catkin_ws/src/wpb_home/wpb_home_tutorials/maps/', shell=True)
        p_temp.wait()
        p_temp = subprocess.Popen('cp ~/map.yaml ~/catkin_ws/src/wpb_home/wpb_home_tutorials/maps/', shell=True)
        p_temp.wait()
        p_temp = subprocess.Popen('rm ~/waypoints.xml', shell=True)
        p_temp.wait()

        # os.system("gnome-terminal -e 'bash -c \"rosrun map_server map_saver -f map\"'")
        # time.sleep(3)
        # os.system("gnome-terminal -e 'bash -c \"cp ~/map.pgm ~/catkin_ws/src/team_108/maps/\"'")
        # os.system("gnome-terminal -e 'bash -c \"cp ~/map.yaml ~/catkin_ws/src/team_108/maps/\"'")
        # os.system("gnome-terminal -e 'bash -c \"cp ~/map.pgm ~/catkin_ws/src/wpb_home/wpb_home_tutorials/maps/\"'")
        # os.system("gnome-terminal -e 'bash -c \"cp ~/map.yaml ~/catkin_ws/src/wpb_home/wpb_home_tutorials/maps/\"'")
        # time.sleep(3)
        p_temp = subprocess.Popen('rosnode kill rviz', shell=True)
        p_temp.wait()

    if str == 'move_forward':
        if p_move is None:
            p_move = subprocess.Popen('rosrun team_108 go_forward',shell=True)
        else:
            if p_move.poll() is None:
                p_move.kill()
            p_move = subprocess.Popen('rosrun team_108 go_forward',shell=True)

    if str == 'move_backward':
        if p_move is None:
            p_move = subprocess.Popen('rosrun team_108 go_backward',shell=True)
        else:
            if p_move.poll() is None:
                p_move.kill()
            p_move = subprocess.Popen('rosrun team_108 go_backward',shell=True)

    if str == 'move_left':
        if p_move is None:
            p_move = subprocess.Popen('rosrun team_108 go_left',shell=True)
        else:
            if p_move.poll() is None:
                p_move.kill()
            p_move = subprocess.Popen('rosrun team_108 go_left',shell=True)

    if str == 'move_right':
        if p_move is None:
            p_move = subprocess.Popen('rosrun team_108 go_right',shell=True)
        else:
            if p_move.poll() is None:
                p_move.kill()
            p_move = subprocess.Popen('rosrun team_108 go_right',shell=True)

    if str == 'rotateleft':
        if p_move is None:
            p_move = subprocess.Popen('rosrun team_108 turn_left',shell=True)
        else:
            if p_move.poll() is None:
                p_move.kill()
            p_move = subprocess.Popen('rosrun team_108 turn_left',shell=True)

    if str == 'rotateright':
        if p_move is None:
            p_move = subprocess.Popen('rosrun team_108 turn_right',shell=True)
        else:
            if p_move.poll() is None:
                p_move.kill()
            p_move = subprocess.Popen('rosrun team_108 turn_right',shell=True)

    if str == 'stop':
        p_temp = subprocess.Popen('rosnode kill rviz',shell=True)
        p_temp.wait()
        p_move = subprocess.Popen('rosrun team_108 stop',shell=True)

    if 'grab' in str:
        p_temp = subprocess.Popen('rosnode kill rviz', shell=True)
        p_temp.wait()
        os.system("gnome-terminal -e 'bash -c \"roslaunch team_108 script_add1.launch\"'")

    if 'navigation' in str:
        p_temp = subprocess.Popen('rosnode kill rviz', shell=True)
        p_temp.wait()
        os.system("gnome-terminal -e 'bash -c \"roslaunch team_108 script_add2.launch\"'")

    if 'follow' in str:
        p_temp = subprocess.Popen('rosnode kill rviz', shell=True)
        p_temp.wait()
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_apps shopping.launch\"'")





def tcplink():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    winip = '192.168.43.6'
    linuxip = '192.168.43.229'
    s.bind((linuxip, 9999))
    s.listen(1)
    while True:
        print('waiting for connection.....')
        sock, addr = s.accept()
        print('Accept new connection from %s:%s...' % addr)
        try:
            data = sock.recv(1024)
            rcvStr = data.decode('utf-8')
            if (rcvStr == 'end'):
                sock.close()
                break
            sendStr = 'received: ' + rcvStr + '\r\n'
            str2shell2(rcvStr)
            sock.send(sendStr.encode('utf-8'))
            print(sendStr.replace('\r\n', ''))
            sock.close()
        except ConnectionAbortedError as e:
            print('Connection Aborted!')
        finally:
            print('Connection from %s:%s closed.' % addr)
    s.shutdown(2)
    s.close()

p_move = None
p_map = None
p_grab = None
p_navi = None
tcplink()



