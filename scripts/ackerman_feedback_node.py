#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import numpy as np
from std_msgs.msg import Header
from geometry_msgs.msg import Twist
from control_msgs.msg import SteeringControllerStatus
import time
from rclpy.parameter import Parameter

from ackermann_interfaces.msg import AckermannFeedback

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        # self.vel_cmd_sub = self.create_subscription(Twist,'/cmd_vel_joy', self.vel_callback, 10)   
        # self.vel_cmd_sub  # prevent unused variable warning

        self.set_parameters([Parameter('use_sim_time', Parameter.Type.BOOL, True)])
        self.steer_sub = self.create_subscription(SteeringControllerStatus,'/diff_cont/controller_state', self.steer_callback, 10 )
        self.prev_wheels_pos = np.array([0,0], dtype=float)
        self.set_parameters([])
        self.prev_time = time.time()
        wheel_radius = 0.056
        tics_in_meter = 17
        wheel_rev_per_meter = 1 / (2*np.pi* wheel_radius)
        tics_in_rev = tics_in_meter / wheel_rev_per_meter 
        self.tics_per_rev_Per_2rad_per_sec = 2*np.pi/ tics_in_rev 

        self.publisher_ = self.create_publisher(AckermannFeedback ,'feedback', 10)
        self.time_period = 0.01

        self.timer = self.create_timer(self.time_period, self.timer_callback)
        self.steer_angle = 0.0


    def timer_callback(self):
        header = Header()
        header.frame_id = 'odom'
        header.stamp = self.get_clock().now().to_msg()
        msg = AckermannFeedback()
        msg.header = header
        try:
            msg.steering_angle = self.steer_angle
        except:
            msg.steering_angle = 0.0
        try:
            msg.left_wheel_speed = self.left_vel
            msg.right_wheel_speed = self.rigth_vel
        except:
            msg.left_wheel_speed = 0.0
            msg.right_wheel_speed = 0.0
        self.publisher_.publish(msg)

    # def vel_callback(self, msg):
    #     linear_velocity_cmd = msg.linear.x

    def steer_callback(self, msg):
        self.steer_angle = sum(msg.steer_positions) / 2
        self.current_wheels_pos = np.array(msg.traction_wheels_position, dtype=float)
        now = time.time()
        delta_t = now - self.prev_time
        self.prev_time = now
        self.current_angular_wheels_vel = ((self.current_wheels_pos - self.prev_wheels_pos) / delta_t ) * self.tics_per_rev_Per_2rad_per_sec
        self.prev_wheels_pos = self.current_wheels_pos
        self.rigth_vel, self.left_vel  = self.current_angular_wheels_vel[0], self.current_angular_wheels_vel[1]
        # print(self.current_angular_wheels_vel)


def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()