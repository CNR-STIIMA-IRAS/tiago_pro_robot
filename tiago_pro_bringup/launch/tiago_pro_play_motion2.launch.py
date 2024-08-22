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

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch.actions import DeclareLaunchArgument, SetLaunchConfiguration, OpaqueFunction

from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.robot_arguments import CommonArgs

from tiago_pro_description.launch_arguments import TiagoProArgs
from tiago_pro_description.tiago_pro_launch_utils import get_tiago_pro_hw_suffix
from dataclasses import dataclass
from launch_pal.param_utils import merge_param_files
import os


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    arm_type_right: DeclareLaunchArgument = TiagoProArgs.arm_type_right
    arm_type_left: DeclareLaunchArgument = TiagoProArgs.arm_type_left
    end_effector_right: DeclareLaunchArgument = TiagoProArgs.end_effector_right
    end_effector_left: DeclareLaunchArgument = TiagoProArgs.end_effector_left
    ft_sensor_right: DeclareLaunchArgument = TiagoProArgs.ft_sensor_right
    ft_sensor_left: DeclareLaunchArgument = TiagoProArgs.ft_sensor_left

    use_sim_time:  DeclareLaunchArgument = CommonArgs.use_sim_time


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):
    play_motion2 = include_scoped_launch_py_description(
        pkg_name='play_motion2',
        paths=['launch', 'play_motion2.launch.py'],
        launch_arguments={
            "use_sim_time":  launch_args.use_sim_time,
            "motions_file": LaunchConfiguration('motions_file'),
            'motion_planner_config': LaunchConfiguration('motion_planner_config')
        })

    launch_description.add_action(OpaqueFunction(
        function=create_play_motion_filename))
    launch_description.add_action(play_motion2)

    return


def create_play_motion_filename(context):

    pkg_name = 'tiago_pro_bringup'
    pkg_share_dir = get_package_share_directory(pkg_name)
    arm_right = read_launch_argument('arm_type_right', context)
    ee_right = read_launch_argument('end_effector_right', context)
    arm_left = read_launch_argument('arm_type_left', context)
    ee_left = read_launch_argument('end_effector_left', context)

    hw_suffix = get_tiago_pro_hw_suffix(
        arm_right=arm_right,
        arm_left=arm_left,
        end_effector_right=ee_right,
        end_effector_left=ee_left,
        ft_sensor_right=read_launch_argument('ft_sensor_right', context),
        ft_sensor_left=read_launch_argument('ft_sensor_left', context),
    )

    # Determine the necessary motions
    ee_motions_paths = []
    motions_folder = os.path.join(pkg_share_dir, 'config', 'motions')
    if arm_right != 'no-arm' and arm_left != 'no-arm':
        base_motions_file = 'tiago_pro_motions_general.yaml'
        if ee_right != 'no-end-effector':
            ee_motions_paths.append(f"tiago_pro_motions_{ee_right}_right.yaml")
        if ee_left != 'no-end-effector':
            ee_motions_paths.append(f"tiago_pro_motions_{ee_left}_left.yaml")
    elif arm_left != 'no-arm':
        base_motions_file = 'tiago_pro_motions_general_arm_left.yaml'
        if ee_left != 'no-end-effector':
            ee_motions_paths.append(f"tiago_pro_motions_{ee_left}_left.yaml")
    elif arm_right != 'no-arm':
        base_motions_file = 'tiago_pro_motions_general_arm_right.yaml'
        if ee_right != 'no-end-effector':
            ee_motions_paths.append(f"tiago_pro_motions_{ee_right}_right.yaml")
    else:
        base_motions_file = 'tiago_pro_motions_no_arms.yaml'

    ee_motions_yamls = []
    for ee_motions_path in ee_motions_paths:
        ee_motions_yamls.append(os.path.join(motions_folder, ee_motions_path))

    # Combine all the config file
    base_motions_yaml = os.path.join(motions_folder, base_motions_file)
    motions_yamls = [base_motions_yaml]
    motions_yamls.extend(ee_motions_yamls)
    motions_config = merge_param_files(motions_yamls)

    motion_planner_file = f"motion_planner{hw_suffix}.yaml"
    motion_planner_config = PathJoinSubstitution([
        pkg_share_dir,
        'config', 'motion_planner', motion_planner_file])

    return [SetLaunchConfiguration("motions_file", motions_config),
            SetLaunchConfiguration("motion_planner_config", motion_planner_config)]


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
