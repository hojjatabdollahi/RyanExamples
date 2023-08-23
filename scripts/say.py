#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from ryan_msgs.msg import Event

class Say:
    def __init__(self):

        rospy.init_node("say_sample", anonymous=True)
        self.pub = rospy.Publisher('/tts_event_topic', Event, queue_size=3)


    def run(self, what_to_say):

        rate = rospy.Rate(1)  # 10hz
        while not rospy.is_shutdown():
            connections = self.pub.get_num_connections()
            rospy.loginfo('Connections: %d', connections)
            if connections > 0:
                msg = Event()
                msg.code = 2000
                msg.source = 1001
                msg.data = "{\"TextInput\":\""+what_to_say+"\",\"Output\":\"\"}"
                self.pub.publish(msg)
                rospy.loginfo('Published')
                break
            rate.sleep()
        
if __name__ == '__main__':
    try:
        s = Say()
        s.run("this is a test")


    except rospy.ROSInterruptException:
        pass



