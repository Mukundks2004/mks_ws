# Instructions For Visualizing Robot


1) Build the workspace/package with `colcon build`
2) Launch the robot_state_publisher launch file with `ros2 launch mks_description rsp.launch.py`
3) Launch joint_state_publisher_gui with `ros2 run joint_state_publisher_gui joint_state_publisher_gui`
4) Launch RViz with `rviz2`

## Configuring RVIZ

1) Set base link to base link (dropdown in top left)
2) Add `RobotModel` display (add button in bottom left)
3) For point #2, set description source to `Topic` and set topic to `/robot_description`

## Useful Debugging Commands:

- `ros2 run xacro xacro /home/mksneo/mks_ws/src/mks_description/urdf/eve.urdf.xacro`

## STL Files

Should go in `/mks_description/meshes` 

You can access them here:
- https://drive.google.com/drive/folders/1dvsBxLHqj5qetu0XFq9vR1L56kMXGcLv?usp=sharing
