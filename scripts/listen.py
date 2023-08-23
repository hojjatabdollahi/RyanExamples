#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from ryan_msgs.msg import Event

class Listen:
    def __init__(self):
        rospy.init_node("listen_sample", anonymous=True)
        self.sub = rospy.Subscriber('/event_topic', Event, self.callback)
        self.pub = rospy.Publisher('/stt_event_topic', Event, queue_size=10)

    def callback(self, data):
        if data.code == 3001:
            rospy.loginfo(data.data)
            rospy.signal_shutdown("Received one message from STT")
    
    def run(self):       
        msg = Event()
        msg.code = 3000
        rate = rospy.Rate(1) 
        while not rospy.is_shutdown():
            connections = self.pub.get_num_connections()
            rospy.loginfo('Connections: %d', connections)
            if connections > 0:
                self.pub.publish(msg)
                rospy.loginfo('Published')
                break
            rate.sleep()

if __name__ == '__main__':
    try:
        l = Listen()
        l.run()
        rospy.spin()

    except rospy.ROSInterruptException:
        pass