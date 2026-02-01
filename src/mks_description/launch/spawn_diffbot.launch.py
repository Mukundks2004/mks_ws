#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    # Robot URDF
    urdf_file = os.path.join(
        get_package_share_directory('mks_description'),
        'urdf',
        'diffbot.urdf'
    )
    with open(urdf_file, 'r') as f:
        robot_description = f.read()

    # Launch Gazebo Sim with an empty world
    ros_gz_sim_pkg = get_package_share_directory('ros_gz_sim')
    gz_sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim_pkg, 'launch', 'gz_sim.launch.py')
        ),
        # Pass empty world as gz_args
        launch_arguments={'gz_args': 'empty.sdf'}.items()
    )

    return LaunchDescription([
        # Gazebo Sim
        gz_sim_launch,

        # Spawn entity after Gazebo starts
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=[
                '-topic', 'robot_description',
                '-name', 'diffbot'
            ],
            output='screen'
        ),

        # Publish robot_description
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description}]
        ),
    ])
