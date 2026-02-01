# #!/usr/bin/env python3

# import os

# from ament_index_python.packages import get_package_share_directory
# from launch import LaunchDescription
# from launch.actions import ExecuteProcess
# from launch_ros.actions import Node

# def generate_launch_description():
#     # Get the path to your URDF
#     urdf_file = os.path.join(
#         get_package_share_directory('mks_description'),
#         'urdf',
#         'diffbot.urdf'
#     )

#     # Read the URDF contents
#     with open(urdf_file, 'r') as infp:
#         robot_description = infp.read()

#     empty_world = os.path.join(
#         get_package_share_directory('ros_gz_sim'),
#         'worlds',
#         'empty.sdf'
#     )

#     return LaunchDescription([
#         # Publish robot description first
#         Node(
#             package='robot_state_publisher',
#             executable='robot_state_publisher',
#             name='robot_state_publisher',
#             output='screen',
#             parameters=[{'robot_description': robot_description}]
#         ),

#         # Start Ignition Gazebo
#         ExecuteProcess(
#             cmd=['gz', 'sim', '-v', '4', empty_world],
#             output='screen'
#         ),


#         # Spawn robot after TF publisher
#         Node(
#             package='ros_gz_sim',
#             executable='create',
#             arguments=['-topic', '/robot_description', '-name', 'diffbot'],
#             output='screen'
#         ),
#     ])

