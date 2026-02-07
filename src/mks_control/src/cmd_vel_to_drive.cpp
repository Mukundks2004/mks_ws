#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "std_msgs/msg/float64.hpp"

class CmdVelToDrive : public rclcpp::Node
{
public:
    CmdVelToDrive() : Node("cmd_vel_to_drive")
    {
        this->declare_parameter<double>("max_linear_speed", 2000.0);
        this->declare_parameter<double>("max_angular_speed", 2000.0);

        max_lin_ = this->get_parameter("max_linear_speed").as_double();
        max_ang_ = this->get_parameter("max_angular_speed").as_double();

        cmd_vel_sub_ = this->create_subscription<geometry_msgs::msg::Twist>(
            "/cmd_vel",
            10,
            std::bind(&CmdVelToDrive::cmdVelCallback, this, std::placeholders::_1)
        );

        fl_pub_ = this->create_publisher<std_msgs::msg::Float64>(
            "front_left/commands/motor/speed", 10);
        fr_pub_ = this->create_publisher<std_msgs::msg::Float64>(
            "front_right/commands/motor/speed", 10);
        rl_pub_ = this->create_publisher<std_msgs::msg::Float64>(
            "rear_left/commands/motor/speed", 10);
        rr_pub_ = this->create_publisher<std_msgs::msg::Float64>(
            "rear_right/commands/motor/speed", 10);
    }

private:
    void cmdVelCallback(const geometry_msgs::msg::Twist::SharedPtr msg)
    {
        double lin_speed = msg->linear.x * max_lin_;
        double ang_speed = msg->angular.z * max_ang_;

        // Skid-steer
        double left_speed  = lin_speed - ang_speed;
        double right_speed = lin_speed + ang_speed;

        std_msgs::msg::Float64 fl, fr, rl, rr;
        fl.data = rl.data = left_speed;
        fr.data = rr.data = right_speed;

        fl_pub_->publish(fl);
        fr_pub_->publish(fr);
        rl_pub_->publish(rl);
        rr_pub_->publish(rr);
    }

    double max_lin_;
    double max_ang_;

    rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr cmd_vel_sub_;
    rclcpp::Publisher<std_msgs::msg::Float64>::SharedPtr fl_pub_, fr_pub_, rl_pub_, rr_pub_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<CmdVelToDrive>());
    rclcpp::shutdown();
    return 0;
}