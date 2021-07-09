#!/usr/bin/bash

colcon build --packages-select ros2_dummy_pkg --symlink-install
source install/local_setup.bash
ros2 run ros2_dummy_pkg node
