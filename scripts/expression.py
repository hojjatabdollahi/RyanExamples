#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from ryan_msgs.msg import Event

Neutral = 0;
Joy = 1;
Sad = 2;
Surprise = 3;
Fear = 4;
Disgust = 5;
Anger = 6;

class Expression:
    def __init__(self):

        rospy.init_node("expression_sample", anonymous=True)
        self.pub = rospy.Publisher('/fxp_event_topic', Event, queue_size=3)


    def run(self, expression):

        rate = rospy.Rate(1)  # 10hz
        while not rospy.is_shutdown():
            connections = self.pub.get_num_connections()
            rospy.loginfo('Connections: %d', connections)
            if connections > 0:
                msg = Event()
                msg.code = 7000
                msg.source = 1003
                msg.data = '{\"Command\":2,\"Expression\":' + str(expression) + ',\"ExpressionIntensity\":0.5,\"ExpressionDuration\"\
                      :2.0,\"OnsetSpeed\":1,\"OffsetSpeed\":1,\"CustomOnsetSpeed\":0.0,\"CustomOffsetSpeed\":0.0}' 
                self.pub.publish(msg)
                rospy.loginfo('Published')
                break
            rate.sleep()
        
if __name__ == '__main__':
    try:
        e = Expression()
        e.run(Joy)


    except rospy.ROSInterruptException:
        pass



