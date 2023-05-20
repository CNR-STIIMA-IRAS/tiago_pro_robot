^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_v2_prototype_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
* Merge branch 'flip_arm_link_3' into 'master'
  remove joy_teleop from bringup and use startup as the incrementer server is...
  See merge request robots/tiago_v2_prototype_robot!6
* added the missing head_action dependency
* Don't start actuator pid controllers and position controllers by default, and handle it by an application
* added the point head action to the default controllers launch file
* load the mobile_base_controller and increase the timeout to 300 seconds
* Contributors: Sai Kishor Kothakota

0.0.3 (2023-05-16)
------------------

0.0.2 (2023-05-16)
------------------

0.0.1 (2023-05-16)
------------------
* Added gravity compensation controller dependency
* Merge branch 'new_v2_bringup' into 'master'
  New v2 bringup and urdf
  See merge request robots/tiago_v2_prototype_robot!1
* Added head_controller to joint_trajectory_controllers.yaml
* Merge branch 'play-motion' into 'new_v2_bringup'
  Play motion
  See merge request robots/tiago_v2_prototype_robot!3
* update the motor torque constants to proper values
* delete files copied from canopies pkgs
* Merge branch 'gripper-integration' into 'new_v2_bringup'
  Grippers integration
  See merge request robots/tiago_v2_prototype_robot!2
* gripper controller params set in the current pkg
* controller added for grippers
* grippers robotiq-2f-85 added for both arms
* Update the motor torque constants for the left and the right arm
* Update the robot model chaines for the gravity compensation controller
* remove the invalid torso_yaw_joint configuration
* reenable right_7_joint
* Disabling arm right 7 temporarily
* Adding missing arm controllers
* added the configuration of the gravity compenesation from canopies configuration
* added the bringup package and the configuration
* update for new arms placement
* Add arm controllers
* First commit
* Contributors: Jordan Palacios, Luca Marchionni, Narcis Miguel, Sai Kishor Kothakota, ileniaperrella
