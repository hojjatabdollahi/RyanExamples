#!/usr/bin/env python
import rospy
from ryan_msgs.srv import TriggerArmGesture


# Gestures
HOME = 100
WAVE_LEFT = 101
WAVE_RIGHT = 102
TAI_CHI = 103
POSE_DOWN = 200
POSE_FORWARD = 201
POSE_SIDE = 202
POSE_OVERHEAD = 203
POSE_FORWARD_CURL = 204
POSE_WIDE_ROW = 205
POSE_OVERHEAD_LOWER = 206

# Results
ACK = 0               # The gesture was accepted and started
BUSY = -1             # Not in a ready state, gesture was refused
INVALID_GESTURE = -2  # Request is not a valid gesture, refused


Status = {
    1: "READY", # Ready to receive a motion command
    0: "ACTIVE", # Currently executing a motion
    -1: "BLOCKED", # Obstacle detected within reach, will not start a new motion
    -2: "COLLISION", # Collision has been detected, trying to recover
    -3: "DISABLED", # Arm servos are disabled
    -4: "ERROR", # Error state
    -5: "DISCONNECTED" # Power lost to servos, estop switch engaged
    }

def exec():
    rospy.wait_for_service('request_arm_gesture')
    try:
        arms_server = rospy.ServiceProxy('request_arm_gesture', TriggerArmGesture)
        response = arms_server(WAVE_RIGHT,4.0)
        if response.result == ACK:
                rospy.loginfo("Done!")
        elif response.result == BUSY:
                rospy.logerr("Arms are busy")
        elif response.result == INVALID_GESTURE:
                rospy.logerr("The gesture is invalid")

        status_index = response.status.status
        rospy.loginfo("Arms status: %s", Status[status_index])


    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
        

        
if __name__ == '__main__':
    rospy.init_node('arms_sample', log_level=rospy.DEBUG)
    exec()



