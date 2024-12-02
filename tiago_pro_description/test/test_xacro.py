# Copyright (c) 2024 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from tiago_pro_description.launch_arguments import TiagoProArgs

from urdf_test.xacro_test import define_xacro_test

xacro_file_path = Path(
    get_package_share_directory('tiago_pro_description'),
    'robots',
    'tiago_pro.urdf.xacro',
)

arm_args = (
    TiagoProArgs.arm_type_right,
    TiagoProArgs.arm_type_left,
)
wrist_args_left = (
    TiagoProArgs.wrist_model_left,
    TiagoProArgs.tool_changer_left,
    TiagoProArgs.ft_sensor_left
)
wrist_args_right = (
    TiagoProArgs.wrist_model_right,
    TiagoProArgs.tool_changer_right,
    TiagoProArgs.ft_sensor_right,
)

gripper_args = (
    TiagoProArgs.end_effector_right,
    TiagoProArgs.end_effector_left,
)

test_xacro_base = define_xacro_test(
    xacro_file_path, arm_args, TiagoProArgs.base_type)
test_xacro_laser = define_xacro_test(
    xacro_file_path, arm_args, TiagoProArgs.laser_model)
test_xacro_ee = define_xacro_test(xacro_file_path, arm_args, gripper_args)
test_xacro_ee = define_xacro_test(
    xacro_file_path, TiagoProArgs.arm_type_left, wrist_args_left)
test_xacro_ee = define_xacro_test(
    xacro_file_path, TiagoProArgs.arm_type_right, wrist_args_right)
test_xacro_ee = define_xacro_test(
    xacro_file_path, TiagoProArgs.end_effector_left, wrist_args_left)
test_xacro_ee = define_xacro_test(
    xacro_file_path, TiagoProArgs.end_effector_right, wrist_args_right)
