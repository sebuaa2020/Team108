#include<iostream>
#include <ros/ros.h> 
#include <std_msgs/String.h>
#include <vector>
#include "action_manager.h"
#include <sound_play/SoundRequest.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib/client/simple_action_client.h>
#include <waterplus_map_tools/GetWaypointByName.h>

using namespace std;

static void Speak(string inStr) {
    sound_play::SoundRequest sp;
    sp.sound = sound_play::SoundRequest::SAY;
    sp.command = sound_play::SoundRequest::PLAY_ONCE;
    sp.arg = inStr;
    spk_pub.publish(sp);
}

int main() {
	assert(Speak("hello").compare("hello") == 0);
	assert(Speak("loser").compare("loser") == 0);
	assert(Speak("Please give me a bottle").compare("Please give me a bottle") == 0);
	assert(Speak("anana").compare("anana") == 0);
	assert(Speak("apple").compare("cat") == 1);
	return 0;
}
