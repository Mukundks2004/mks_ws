from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='cube_detection',
            executable='cube_detector_node',
            name='cube_detector_node',
            output='screen',
            parameters=[{
                'model_path': '/home/yao/models/best.pt',
            }]
        ),
        Node(
            package='cube_detection',
            executable='cube_chase_controller',
            name='cube_chase_controller',
            output='screen',
            parameters=[{
                'cmd_vel_topic': '/cmd_vel',
            }]
        )
    ])