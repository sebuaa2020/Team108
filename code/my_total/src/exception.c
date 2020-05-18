#include <iostream>
#include "exception.h"

void follow_start_fail(){
  cout << "cannot start following!"<< endl;
}

void follow_stop_fail(){
  cout << "cannot stop following" << endl;
}

void goto_fail(){
  cout << "fail to get destination" << endl;
}

void find_waypoint_fail(){
  cout << "fail to find a waypoint" << endl;
}
