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
from launch import LaunchDescription
from launch.actions import GroupAction
from launch_pal.param_utils import merge_param_files

from launch_pal.robot_utils import get_robot_name
from ament_index_python.packages import get_package_share_directory
from controller_manager.launch_utils import generate_load_controller_launch_description


def generate_launch_description():

    pkg_share_folder = get_package_share_directory("tiago_pro_controller_configuration")

    # Mobile base controller
    default_config = os.path.join(
        pkg_share_folder, "config", "mobile_base_controller.yaml"
    )

    calibration_config = "/etc/calibration/master_calibration.yaml"

    if os.path.exists(calibration_config):
        params_file = merge_param_files([default_config, calibration_config])
    else:
        params_file = default_config

    mobile_base_controller_launch = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name="mobile_base_controller",
                controller_type="omni_drive_controller/OmniDriveController",
                controller_params_file=params_file,
            )
        ],
        forwarding=False,
    )

    joint_state_broadcaster_launch = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name="joint_state_broadcaster",
                controller_type="joint_state_broadcaster/JointStateBroadcaster",
                controller_params_file=os.path.join(
                    pkg_share_folder, "config", "joint_state_broadcaster.yaml"
                ),
            )
        ],
        forwarding=False,
    )

    torso_controller_launch = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name="torso_controller",
                controller_type="joint_trajectory_controller/JointTrajectoryController",
                controller_params_file=os.path.join(
                    pkg_share_folder, "config", "torso_controller.yaml"
                ),
            )
        ],
        forwarding=False,
    )

    head_controller_launch = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name="head_controller",
                controller_type="joint_trajectory_controller/JointTrajectoryController",
                controller_params_file=os.path.join(
                    pkg_share_folder, "config", "head_controller.yaml"
                ),
            )
        ],
        forwarding=False,
    )

    arm_right_controller_launch = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name="arm_right_controller",
                controller_type="joint_trajectory_controller/JointTrajectoryController",
                controller_params_file=os.path.join(
                    pkg_share_folder, "config", "arm_right_controller.yaml"
                ),
            )
        ],
        forwarding=False,
    )

    arm_left_controller_launch = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name="arm_left_controller",
                controller_type="joint_trajectory_controller/JointTrajectoryController",
                controller_params_file=os.path.join(
                    pkg_share_folder, "config", "arm_left_controller.yaml"
                ),
            )
        ],
        forwarding=False,
    )

    end_effector_right_controller_launch = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name="gripper_right_controller",
                controller_type="joint_trajectory_controller/JointTrajectoryController",
                controller_params_file=os.path.join(
                    pkg_share_folder, "config", "gripper_right_controller.yaml"
                ),
            )
        ],
        forwarding=False,
    )

    end_effector_left_controller_launch = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name="gripper_left_controller",
                controller_type="joint_trajectory_controller/JointTrajectoryController",
                controller_params_file=os.path.join(
                    pkg_share_folder, "config", "gripper_left_controller.yaml"
                ),
            )
        ],
        forwarding=False,
    )

    ld = LaunchDescription()

    ld.add_action(get_robot_name("tiago_pro"))

    ld.add_action(joint_state_broadcaster_launch)
    ld.add_action(mobile_base_controller_launch)
    ld.add_action(torso_controller_launch)
    ld.add_action(head_controller_launch)
    ld.add_action(arm_right_controller_launch)
    ld.add_action(arm_left_controller_launch)
    ld.add_action(end_effector_right_controller_launch)
    ld.add_action(end_effector_left_controller_launch)

    return ld
