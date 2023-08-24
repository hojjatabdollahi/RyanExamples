#!/usr/bin/env python
import rospy
from ryan_msgs.srv import UpdateNeckMotion
from ryan_msgs.msg import MotionCommand
from trajectory_msgs.msg import JointTrajectoryPoint



# Error codes
error_codes = {
        0: "SUCCESSFUL",
        -1: "ERROR",
        -2: "INVALID_TRAJECTORIES",
        -3: "INVALID_REQUEST",
        -4: "INVALID_RESPONSE"
    }

# Motion Command
POSTURE = 1
GESTURE = 2
BOTH = 3




def posture():

    rospy.wait_for_service('update_neck_motion')
    try:
        neck_server = rospy.ServiceProxy('update_neck_motion', UpdateNeckMotion)


        desired_motion = MotionCommand()
        desired_motion.type = POSTURE
        desired_motion.merge = False

        # desired_posture = JointTrajectoryPoint()
        # roll = 0.0 # tiliting the head left or right, (rarely used)
        # pitch = 0.0 # looking up or down, 0.0 is straight ahead
        # yaw = -0.3 # looking to the left or right, 0.0 is straight ahead
        # desired_posture.positions = [roll, pitch, yaw] 
        # desired_posture.time_from_start = rospy.Duration(1.0)
        # desired_motion.posture = desired_posture

        LOOK_LEFT = JointTrajectoryPoint(positions=[0.0, 0.0, -0.3], time_from_start=rospy.Duration(2.0))
        LOOK_RIGHT = JointTrajectoryPoint(positions=[0.0, 0.0, 0.3], time_from_start=rospy.Duration(2.0))
        desired_motion.posture = LOOK_RIGHT


        response = neck_server(desired_motion)
        rospy.loginfo("response: %s", error_codes[response.error_code])


    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
        
def gesture():

    rospy.wait_for_service('update_neck_motion')
    try:
        neck_server = rospy.ServiceProxy('update_neck_motion', UpdateNeckMotion)



        desired_motion = MotionCommand()
        desired_motion.type = GESTURE
        desired_motion.merge = True

        NOD = 1
        HEADBANG = 2
        EX_NOD = 3
        TILT = 4
        SURPRISE = 5
        HOLD_SURPRISE = 6
        CIRCLE = 7
        SHAKE = 8
        GLANCE = 9
        desired_motion.gesture.type = SHAKE



        response = neck_server(desired_motion)
        rospy.loginfo("response: %s", error_codes[response.error_code])


    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

        
if __name__ == '__main__':
    rospy.init_node('neck_sample', log_level=rospy.DEBUG)

    # postrure()
    gesture()

