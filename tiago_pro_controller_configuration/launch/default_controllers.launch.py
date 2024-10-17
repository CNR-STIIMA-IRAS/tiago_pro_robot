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

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import GroupAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from controller_manager.launch_utils import generate_load_controller_launch_description
from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.robot_arguments import CommonArgs
from tiago_pro_description.launch_arguments import TiagoProArgs

from dataclasses import dataclass


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    base_type: DeclareLaunchArgument = TiagoProArgs.base_type
    arm_type_right: DeclareLaunchArgument = TiagoProArgs.arm_type_right
    arm_type_left: DeclareLaunchArgument = TiagoProArgs.arm_type_left
    end_effector_right: DeclareLaunchArgument = TiagoProArgs.end_effector_right
    end_effector_left: DeclareLaunchArgument = TiagoProArgs.end_effector_left
    ft_sensor_right: DeclareLaunchArgument = TiagoProArgs.ft_sensor_right
    ft_sensor_left: DeclareLaunchArgument = TiagoProArgs.ft_sensor_left
    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time
    is_public_sim: DeclareLaunchArgument = CommonArgs.is_public_sim
    namespace: DeclareLaunchArgument = CommonArgs.namespace


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    pkg_share_folder = get_package_share_directory(
        'tiago_pro_controller_configuration')

    # Mobile base controller
    launch_description.add_action(
        OpaqueFunction(function=launch_mobile_base_controller))

    # Joint state broadcaster
    joint_state_broadcaster = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='joint_state_broadcaster',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'joint_state_broadcaster.yaml'))
         ],
        forwarding=False)

    launch_description.add_action(joint_state_broadcaster)

    # Torso controller
    torso_controller = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='torso_controller',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'torso_controller.yaml'))
         ],
        forwarding=False)

    launch_description.add_action(torso_controller)

    # Head controller
    head_controller = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='head_controller',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'head_controller.yaml'))
         ],
        forwarding=False)

    launch_description.add_action(head_controller)

    # IMU sensor broadcaster
    imu_sensor_broadcaster = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name='imu_sensor_broadcaster',
                controller_params_file=os.path.join(
                    pkg_share_folder, 'config', 'imu_sensor_broadcaster.yaml'))

        ],
    )
    launch_description.add_action(imu_sensor_broadcaster)

    # Add controller of right arm, end-effector and ft-sensor
    side_controllers = include_scoped_launch_py_description(
        pkg_name='tiago_pro_controller_configuration',
        paths=['launch', 'arm_controllers.launch.py'],
        launch_arguments={'arm_type_right': launch_args.arm_type_right,
                          'arm_type_left': launch_args.arm_type_left,
                          "end_effector_right": launch_args.end_effector_right,
                          "end_effector_left": launch_args.end_effector_left,
                          "ft_sensor_right": launch_args.ft_sensor_right,
                          "ft_sensor_left": launch_args.ft_sensor_left,
                          "namespace": launch_args.namespace,
                          "use_sim_time": launch_args.use_sim_time
                          },
        condition=IfCondition(LaunchConfiguration('use_sim_time'))
    )

    launch_description.add_action(side_controllers)

    # Gravity compensation controller
    gravity_compensation_controller = include_scoped_launch_py_description(
        pkg_name="tiago_pro_controller_configuration",
        paths=["launch", "gravity_compensation_controller.launch.py"],
    )

    launch_description.add_action(gravity_compensation_controller)

    return


def launch_mobile_base_controller(context, *args, **kwargs):

    base_type = read_launch_argument("base_type", context)
    use_sim_time = read_launch_argument("use_sim_time", context)
    is_public_sim = read_launch_argument("is_public_sim", context)

    base_controller_package = base_type + "_controller_configuration"

    mobile_base_controller = include_scoped_launch_py_description(
        pkg_name=base_controller_package,
        paths=["launch", "mobile_base_controller.launch.py"],
        launch_arguments={
            "use_sim_time": use_sim_time,
            "is_public_sim": is_public_sim,
        }
    )

    return [mobile_base_controller]


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
