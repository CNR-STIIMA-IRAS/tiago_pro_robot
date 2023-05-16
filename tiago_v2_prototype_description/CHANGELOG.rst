^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_v2_prototype_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
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
