# Some Commands:

## TESTING CAMERA WORKS

Prereqs:
- `sudo apt install ros-humble-realsense2-camera`
- `sudo apt install ros-humble-rviz2`

Build:
- `colcon build`
- `source install/setup.bash`

Test:
- `lsusb` look for intel

In rviz:
1) add (bottom left) -> image
2) set topic

Optional:
- `ros-humble-rqt-image-view`
- `ros2 run rqt_image_view rqt_image_view /camera/camera/depth/image_rect_raw`
- `ros2 run rqt_image_view rqt_image_view /camera/camera/color/image_raw`

Run:
- `ros2 launch realsense2_camera rs_launch.py`
- `ros2 run rviz2 rviz2`
- `ros2 run environment_mapping pointcloud_accumulator`

## rtabmap

- `sudo apt-get install ros-humble-rtabmap-ros`
- `sudo apt-get install ros-humble-imu-tools`
- `ros2 launch environment_mapping rtabmap_realsense.launch.py`
