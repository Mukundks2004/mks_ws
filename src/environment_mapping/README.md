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
- `ros2 run rqt_image_view rqt_image_view`
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



## Other:
`ros2 launch rtabmap_launch rtabmap.launch.py   rgb_topic:=/camera/color/image_raw   depth_topic:=/camera/depth/image_rect_raw   camera_info_topic:=/camera/color/camera_info   imu_topic:=/camera/imu/data   frame_id:=camera_link   rviz:=true`

```bash
sudo apt update
sudo apt install ros-humble-image-transport \
                 ros-humble-image-transport-plugins \
                 ros-humble-cv-bridge
```

```bash
ros2 launch realsense2_camera rs_launch.py enable_imu:=true enable_accel:=true enable_gyro:=true
```

```bash
ros2 launch realsense2_camera rs_launch.py enable_gyro:=true enable_accel:=true unite_imu_method:=2
```

```bash
ros2 launch rtabmap_launch rtabmap.launch.py \
  rgb_topic:=/camera/camera/color/image_raw \
  depth_topic:=/camera/camera/depth/image_rect_raw \
  camera_info_topic:=/camera/camera/color/camera_info \
  imu_topic:=/camera/camera/imu \
  frame_id:=camera_link
```

```
rtabmap-databaseViewer rtabmap.db
```

## Remapping imu with ekf

```bash
ros2 run imu_filter_madgwick imu_filter_madgwick_node \
  imu_topic:=/camera/camera/imu \
  output_imu_topic:=/imu/data
```

you will get warning
```
[WARN] [1770762405.174334383] [rcl]: Found remap rule 'imu_topic:=/camera/camera/imu'. This syntax is deprecated. Use '--ros-args --remap imu_topic:=/camera/camera/imu' instead.
```

```bash
mv /home/mks/.ros/rtabmap.db /home/mks/my_map.db
```

## To run rtab you need the following
1) camera node
2) madgewick
3) rtabmap itself

## Post processing
1) open database viewer, open .db file
2) export as ply (pointcloud)
3) view in meshlab