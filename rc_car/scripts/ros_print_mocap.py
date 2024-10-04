#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import numpy as np
from mocap_msgs.msg import RigidBodies


class MOCAP(Node):

    def __init__(self):
        super().__init__('mocap')

        self.create_subscription(RigidBodies, '/rigid_bodies',self.feedback_callback,10)
        # self.publisher = self.create_publisher(Twist, '/cmd_vel_joy_inverse', 10)

    def feedback_callback(self, msg):
        print(msg)
    



def main(args=None):
    rclpy.init(args=args)
    mocap_publisher = MOCAP()
    rclpy.spin(mocap_publisher)
    mocap_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
