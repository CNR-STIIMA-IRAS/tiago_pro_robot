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

import os
from pathlib import Path
from typing import Dict

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_param_builder import load_xacro
from launch_pal.arg_utils import read_launch_argument


def generate_launch_description():

    # Create the launch description and populate
    ld = LaunchDescription()

    launch_args = declare_launch_arguments()

    for arg in launch_args.values():
        ld.add_action(arg)

    ld.add_action(OpaqueFunction(function=launch_setup))

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


def launch_setup(context, *args, **kwargs):

    robot_description = {'robot_description': load_xacro(
        Path(os.path.join(
            get_package_share_directory('tiago_pro_description'),
            'robots', 'tiago_pro.urdf.xacro')),
        {
            'end_effector_right': read_launch_argument('end_effector_right', context),
            'end_effector_left': read_launch_argument('end_effector_left', context),
            'ft_sensor_right': read_launch_argument('ft_sensor_right', context),
            'ft_sensor_left': read_launch_argument('ft_sensor_left', context),
            'laser_model': read_launch_argument('laser_model', context),
            'use_sim': read_launch_argument('use_sim_time', context),
            'namespace': read_launch_argument('namespace', context),
        }
    )}

    rsp = Node(package='robot_state_publisher',
               executable='robot_state_publisher',
               output='both',
               parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')},
                           robot_description])

    return [rsp]
