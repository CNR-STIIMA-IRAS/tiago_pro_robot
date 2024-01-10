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
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument

from launch_pal.include_utils import include_launch_py_description


def generate_launch_description():

    ld = LaunchDescription()

    declare_launch_arguments(ld)
    declare_actions(ld)
    return ld


def declare_launch_arguments(launch_description: LaunchDescription):

    sim_time_arg = DeclareLaunchArgument(
        'use_sim_time', default_value='False',
        description='Use sim time. ')

    launch_description.add_action(sim_time_arg)

    robot_name = DeclareLaunchArgument(
        'robot_name',
        default_value='tiago_pro',
        description='Name of the robot. ',
        choices=['pmb2', 'tiago', 'pmb3', 'tiago_dual', 'tiago_pro'])

    launch_description.add_action(robot_name)

    end_effector_right = DeclareLaunchArgument(
        'end_effector_right',
        default_value='pal-pro-gripper',
        description='End effector model of the right arm.',
        choices=['pal-pro-gripper', 'no-ee'])

    launch_description.add_action(end_effector_right)

    end_effector_left = DeclareLaunchArgument(
        'end_effector_left',
        default_value='pal-pro-gripper',
        description='End effector model of the left arm.',
        choices=['pal-pro-gripper', 'no-ee'])

    launch_description.add_action(end_effector_left)

    ft_sensor_right = DeclareLaunchArgument(
        'ft_sensor_right',
        default_value='rokubi',
        description='FT sensor model. ',
        choices=['rokubi', 'no-ft-sensor'])

    launch_description.add_action(ft_sensor_right)

    ft_sensor_left = DeclareLaunchArgument(
        'ft_sensor_left',
        default_value='rokubi',
        description='FT sensor model. ',
        choices=['rokubi', 'no-ft-sensor'])

    launch_description.add_action(ft_sensor_left)

    return


def declare_actions(launch_description: LaunchDescription):

    motions_yaml = 'tiago_pro_motions.yaml'

    play_motion2_config = os.path.join(
        get_package_share_directory('tiago_pro_bringup'), 'config', 'motions', motions_yaml)

    play_motion2 = include_launch_py_description(
        'play_motion2', ['launch', 'play_motion2.launch.py'],
        launch_arguments={'play_motion2_config': play_motion2_config}.items())

    launch_description.add_action(play_motion2)

    return
