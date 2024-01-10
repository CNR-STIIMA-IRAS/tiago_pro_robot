# Copyright (c) 2023 PAL Robotics S.L. All rights reserved.
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

from typing import Dict
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction
from controller_manager.launch_utils import generate_load_controller_launch_description
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PythonExpression


def generate_launch_description():

    # Create the launch description and populate
    ld = LaunchDescription()

    launch_args = declare_launch_arguments()

    for arg in launch_args.values():
        ld.add_action(arg)

    declare_actions(ld, launch_args)

    return ld


def declare_launch_arguments() -> Dict:

    arg_dict = {}

    use_sim_time = DeclareLaunchArgument(
        'use_sim_time', default_value='false',
        description='Use simulation time')

    arg_dict[use_sim_time.name] = use_sim_time

    robot_name = DeclareLaunchArgument(
        'robot_name',
        default_value='tiago_pro',
        description='Name of the robot. ',
        choices=['pmb2', 'tiago', 'pmb3', 'tiago_dual', 'tiago_pro'])

    arg_dict[robot_name.name] = robot_name

    end_effector_right = DeclareLaunchArgument(
        'end_effector_right',
        default_value='pal-pro-gripper',
        description='End effector model of the right arm.',
        choices=['pal-pro-gripper', 'no-ee'])

    arg_dict[end_effector_right.name] = end_effector_right

    end_effector_left = DeclareLaunchArgument(
        'end_effector_left',
        default_value='pal-pro-gripper',
        description='End effector model of the left arm.',
        choices=['pal-pro-gripper', 'no-ee'])

    arg_dict[end_effector_left.name] = end_effector_left

    ft_sensor_right = DeclareLaunchArgument(
        'ft_sensor_right',
        default_value='rokubi',
        description='FT sensor model. ',
        choices=['rokubi', 'no-ft-sensor'])

    arg_dict[ft_sensor_right.name] = ft_sensor_right

    ft_sensor_left = DeclareLaunchArgument(
        'ft_sensor_left',
        default_value='rokubi',
        description='FT sensor model. ',
        choices=['rokubi', 'no-ft-sensor'])

    arg_dict[ft_sensor_left.name] = ft_sensor_left

    laser_model = DeclareLaunchArgument(
        'laser_model',
        default_value='sick-571',
        description='Base laser model. ',
        choices=['no-laser', 'sick-571', 'sick-561', 'sick-551', 'hokuyo'])

    arg_dict[laser_model.name] = laser_model

    namespace = DeclareLaunchArgument(
        'namespace',
        default_value='',
        description='Define namespace of the robot. ')

    arg_dict[namespace.name] = namespace

    return arg_dict


def declare_actions(launch_description: LaunchDescription, launch_args: Dict):

    # TODO: mobile_base_controller

    pkg_share_folder = get_package_share_directory(
        'tiago_pro_controller_configuration')

    joint_state_broadcaster = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='joint_state_broadcaster',
            controller_type='joint_state_broadcaster/JointStateBroadcaster',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'joint_state_broadcaster.yaml'))
         ],
        forwarding=False)

    launch_description.add_action(joint_state_broadcaster)

    torso_controller = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='torso_controller',
            controller_type='joint_trajectory_controller/JointTrajectoryController',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'torso_controller.yaml'))
         ],
        forwarding=False)

    launch_description.add_action(torso_controller)

    head_controller = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='head_controller',
            controller_type='joint_trajectory_controller/JointTrajectoryController',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'head_controller.yaml'))
         ],
        forwarding=False)

    launch_description.add_action(head_controller)

    arm_right_controller = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='arm_right_controller',
            controller_type='joint_trajectory_controller/JointTrajectoryController',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'arm_right_controller.yaml'))
         ],
        forwarding=False)

    launch_description.add_action(arm_right_controller)

    arm_left_controller = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='arm_left_controller',
            controller_type='joint_trajectory_controller/JointTrajectoryController',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'arm_left_controller.yaml'))
         ],
        forwarding=False)

    launch_description.add_action(arm_left_controller)

    end_effector_right_controller = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='gripper_right_controller',
            controller_type='joint_trajectory_controller/JointTrajectoryController',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'gripper_right_controller.yaml'))
         ],
        forwarding=False,
        condition=IfCondition(
            PythonExpression(
                ["'", LaunchConfiguration(
                    'end_effector_right'), "' != 'no-ee'"]
            )
        ))
    launch_description.add_action(end_effector_right_controller)

    end_effector_left_controller = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='gripper_left_controller',
            controller_type='joint_trajectory_controller/JointTrajectoryController',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'gripper_left_controller.yaml'))
         ],
        forwarding=False,
        condition=IfCondition(
            PythonExpression(
                ["'", LaunchConfiguration(
                    'end_effector_left'), "' != 'no-ee'"]
            )
        ))
    launch_description.add_action(end_effector_left_controller)

    return
