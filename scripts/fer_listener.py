#!/usr/bin/env python
  
import rospy
from ryan_msgs.msg import FER

Emotions = ["Neutral", "Happy", "Sad", "Angry"]  
  
def callback(data):

    if data.Emotion < len(Emotions):      
        rospy.loginfo("%s", Emotions[data.Emotion])
    else:
        rospy.loginfo("Unknown emotion")
  
  
def main():
    rospy.init_node('fer_listener', anonymous=True)
    rospy.Subscriber("/fer_event_topic", FER, callback)
    rospy.spin()
  
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass