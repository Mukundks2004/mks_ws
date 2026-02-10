import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import random
import time

class AutoVelocityControl(Node):
    def __init__(self):
        super().__init__('auto_velocity_control')

        # Declare parameters for max speeds
        self.declare_parameter('max_linear_speed', 2000.0)
        self.declare_parameter('max_angular_speed', 2000.0)

        # Get the parameters
        self.max_lin_ = self.get_parameter('max_linear_speed').value
        self.max_ang_ = self.get_parameter('max_angular_speed').value

        # Publishers for each wheel's motor speed command
        self.fl_pub_ = self.create_publisher(Float64, 'front_left/commands/motor/speed', 10)
        self.fr_pub_ = self.create_publisher(Float64, 'front_right/commands/motor/speed', 10)
        self.rl_pub_ = self.create_publisher(Float64, 'rear_left/commands/motor/speed', 10)
        self.rr_pub_ = self.create_publisher(Float64, 'rear_right/commands/motor/speed', 10)

        # Timer to change velocity and steering every 5 seconds
        self.timer = self.create_timer(5.0, self.publish_random_velocity)

    def publish_random_velocity(self):
        # Randomize linear and angular speeds (3-8% of max speeds)
        lin_speed = self.get_random_speed(self.max_lin_)
        ang_speed = self.get_random_speed(self.max_ang_)

        # Skid-steer: left = lin - ang, right = lin + ang
        left_speed = lin_speed - ang_speed
        right_speed = lin_speed + ang_speed

        # Prepare messages
        fl_msg = Float64()
        fr_msg = Float64()
        rl_msg = Float64()
        rr_msg = Float64()

        fl_msg.data = left_speed
        rl_msg.data = left_speed
        fr_msg.data = right_speed
        rr_msg.data = right_speed

        # Publish to motors
        self.fl_pub_.publish(fl_msg)
        self.fr_pub_.publish(fr_msg)
        self.rl_pub_.publish(rl_msg)
        self.rr_pub_.publish(rr_msg)

        # Log the velocity to ROS
        self.get_logger().info(f'Published velocities - Left: {left_speed}, Right: {right_speed}')

    def get_random_speed(self, max_speed):
        # Generate random speed in the range [min_pct, max_pct] of the max speed
        min_pct = 0.03  # 3% of max speed
        max_pct = 0.08  # 8% of max speed
        random_pct = random.uniform(min_pct, max_pct)
        return random_pct * max_speed


def main(args=None):
    rclpy.init(args=args)

    auto_velocity_control = AutoVelocityControl()

    try:
        rclpy.spin(auto_velocity_control)
    except KeyboardInterrupt:
        pass
    finally:
        auto_velocity_control.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
