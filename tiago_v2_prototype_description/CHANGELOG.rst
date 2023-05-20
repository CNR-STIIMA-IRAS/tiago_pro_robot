^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_v2_prototype_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
* Merge branch 'flip_arm_link_3' into 'master'
  remove joy_teleop from bringup and use startup as the incrementer server is...
  See merge request robots/tiago_v2_prototype_robot!6
* added realsense2_description dependency
* added head_screen_link to the URDF
* Merge branch 'head-camera' into 'flip_arm_link_3'
  Head camera integration
  See merge request robots/tiago_v2_prototype_robot!5
* intel d435 added
* 180 degrees flip of link 3 to improve motion ranges
* Contributors: Luca Marchionni, Sai Kishor Kothakota, ileniaperrella

0.0.3 (2023-05-16)
------------------

0.0.2 (2023-05-16)
------------------
* remove unused tiago_sea_arm_description dependency
* Contributors: Sai Kishor Kothakota

0.0.1 (2023-05-16)
------------------
* Merge branch 'new_v2_bringup' into 'master'
  New v2 bringup and urdf
  See merge request robots/tiago_v2_prototype_robot!1
* Added gazebo flags for joint and reformat dynamic parameters for ars, head and torso
* remove log file
* Reduce head joint limits and update dynamic parameters
* Flip joint_2 limits
* Merge branch 'gripper-integration' into 'new_v2_bringup'
  Grippers integration
  See merge request robots/tiago_v2_prototype_robot!2
* grippers robotiq-2f-85 added for both arms
* update joint position limtis
* removed not used mesh folders
* Install gazebo directory too
* Cleaning and simplification of collision meshes
* fixed inertia and joints naming
* both arms fixed and tool link added
* First v2 proto alsmost working version
* update for new arms placement
* test manipulability with moveit and workspace
* Configuration with arm in the front and pointing down
* Added params for arm placement and params in launch files
* Mounting pose of the arms in an external file
* Update rviz config file
* Use reflect param
* Add gazebo plugins
* First commit
* Contributors: Jordan Palacios, Luca Marchionni, Narcis Miguel, Sai Kishor Kothakota, ileniaperrella
