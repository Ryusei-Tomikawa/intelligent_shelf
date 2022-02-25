#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

if __name__ == '__main__':
    rospy.init_node('move_shelf')

    shelf_top_pub = rospy.Publisher('/shelf_top_position_controller/command', Float64, queue_size=10)
    shelf_middle_pub = rospy.Publisher('/shelf_middle_position_controller/command', Float64, queue_size=10)
    shelf_bottom_pub = rospy.Publisher('/shelf_bottom_position_controller/command', Float64, queue_size=10)

    r = rospy.Rate(100)
    
    msg = Float64()
    rospy.loginfo("Move shelf Start")

    while not rospy.is_shutdown():

        rospy.loginfo("Please input bottom or middle or top or reset!")
        num = raw_input()
        msg.data = 0.33
        if num == "bottom":
            shelf_bottom_pub.publish(msg)
            rospy.loginfo("Move shelf Done")
        elif num == "middle":
            shelf_middle_pub.publish(msg)
            rospy.loginfo("Move shelf Done")
        elif num == "top":
            shelf_top_pub.publish(msg)
            rospy.loginfo("Move shelf Done")
        elif num == "reset":
            msg.data = 0
            shelf_bottom_pub.publish(msg)
            shelf_middle_pub.publish(msg)
            shelf_top_pub.publish(msg)
            rospy.loginfo("Move shelf Done")
        else:
            rospy.loginfo("No ...")
            break
        r.sleep()
