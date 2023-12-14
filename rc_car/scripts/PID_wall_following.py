#!/usr/bin/env python3

import rclpy
from sensor_msgs.msg import LaserScan
from rclpy.node import Node
from geometry_msgs.msg import Twist
import numpy as np

class PID(object):
    def __init__(self):
        self.error = 0
        self.prev_time = 0
        self.Prev_error = 0
        self.Integral = 0
        self.kp = 1
        self.kd = 0
        self.ki = 0
        self.time = 0
    
    def pid_step(self, ref, current):
        self.error = current - ref
        delta_t = 0
        u = self.error * self.kp + (self.error - self.Prev_error) * self.kd / delta_t + self.Integral * self.ki
        self.Prev_error = self.error
        self.Integral += self.error * delta_t
        return u






class WALL_FOLLOWING(Node):
    '''
    this node takes as input steering angle and radial velocity of the rear wheel
    and convert it to twist_msg
    '''
    def __init__(self):
        super().__init__('inverse_twist')
 
        
        self.create_subscription(LaserScan, '/scan',self.feedback_callback,10)
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        
        self.pid = PID()
        self.wheel_radius = 0.056
        self.wheelbase = 0.3429
        # if max_steering_angle changed the value in ROS_ARDUINO_BRIDGE must be changed too!
        self.max_steering_angle = 0.6 #  = 35[deg] * np.pi / 180
        max_linear_velocity = 2
        self.max_radial_velocity_rear_wheel = max_linear_velocity / self.wheel_radius 

    def feedback_callback(self, msg:LaserScan):
        right_beam = msg.ranges[90]
        theta = 45
        theta_rad = theta * np.pi / 180
        offset_beam = msg.ranges[90+theta] 
        alpha = np.arctan((offset_beam*np.cos(theta_rad) - right_beam) / (offset_beam*np.sin(theta_rad)))
        dist2wall = right_beam * np.cos(alpha)
        L = 1.5
        predicted_dist2wall = dist2wall + L * np.sin(alpha)
        self.pid.pid_step(ref=1.0 , current=predicted_dist2wall )
       



        
    
   
    def publish_steering_cmd(self, steering_angle):
        rear_wheel_w = self.max_radial_velocity_rear_wheel
        steering_angle  = steering_angle
        cmd_vel = Twist()
        cmd_vel.linear.x = rear_wheel_w * self.wheel_radius * np.cos(steering_angle) 
        cmd_vel.linear.y = 0.0
        cmd_vel.linear.z = 0.0
        cmd_vel.angular.x = 0.0
        cmd_vel.angular.y = 0.0
        cmd_vel.angular.z = cmd_vel.linear.x * np.tan(steering_angle) / self.wheelbase
        self.publisher.publish(cmd_vel)


def main(args=None):
    rclpy.init(args=args)
    wall_following = WALL_FOLLOWING()
    rclpy.spin(wall_following)
    wall_following.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
