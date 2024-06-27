^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_pro_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
* Merge branch 'dtk/fix-gazebo-urdf' into 'humble-devel'
  Dtk/fix gazebo urdf
  See merge request robots/tiago_pro_robot!51
* Change occurences of sim_time to use_sim_time
* Move remove global gazebo.urdf file
* Contributors: David ter Kuile, davidterkuile

1.0.11 (2024-06-26)
-------------------
* Merge branch 'dtk/move-robot-args' into 'humble-devel'
  Change import for launch args
  See merge request robots/tiago_pro_robot!50
* Add is missing is_multiple xacro arg
* Change import for launch args
* Contributors: David ter Kuile, davidterkuile

1.0.10 (2024-05-22)
-------------------
* Merge branch 'dtk/fix/head-camera-name' into 'humble-devel'
  Change camera name and topic to head_front_camera
  See merge request robots/tiago_pro_robot!40
* Change camera name and topic to head_front_camera
* Merge branch 'smd/feat/realsense_calibrated' into 'humble-devel'
  Added calibrated tf realsense for the real robot
  See merge request robots/tiago_pro_robot!42
* Added calibrated tf realsense for the real robot
* Contributors: David ter Kuile, davidterkuile, sergiomoyano

1.0.9 (2024-05-09)
------------------
* Merge branch 'omm/feat/arm_name_std' into 'humble-devel'
  Changed arm_model to arm_type in the URDF
  See merge request robots/tiago_pro_robot!39
* Changed arm_model to arm_type in the URDF
* Contributors: davidterkuile, oscarmartinez

1.0.8 (2024-04-26)
------------------
* Fix typo
* Contributors: davidterkuile

1.0.7 (2024-04-18)
------------------
* Merge branch 'omm/feat/public_sim_check' into 'humble-devel'
  Public Sim check
  See merge request robots/tiago_pro_robot!36
* is_public_sim support in launch files
* urdf support for is_public_sim
* Merge branch 'omm/fix/urdf_proper_structure' into 'humble-devel'
  Robot urdf reestructured
  See merge request robots/tiago_pro_robot!35
* Loading calibration constants properly
* Robot urdf reestructured
* Contributors: Oscar, davidterkuile

1.0.6 (2024-04-17)
------------------
* Merge branch 'omm/fix/default_laser' into 'humble-devel'
  Fixed default laser value
  See merge request robots/tiago_pro_robot!34
* Small reorganization of the urdf
* Changed default laser
* Applying autoformater
* Contributors: Oscar, davidterkuile

1.0.5 (2024-04-16)
------------------
* Merge branch 'fix/ros-planar-move-rate' into 'humble-devel'
  modified gazebo ros_planar_move rate
  See merge request robots/tiago_pro_robot!33
* modified gazebo ros_planar_move rate
* Merge branch 'dtk/feat/add-modules' into 'humble-devel'
  Dtk/feat/add modules
  See merge request robots/tiago_pro_robot!32
* Change module number prefix to 10
* Add modules
* Merge branch 'omm/fix/spinning_tiago' into 'humble-devel'
  Restored ros_planar_move plugin
  See merge request robots/tiago_pro_robot!31
* Restored ros_planar_move plugin
* Contributors: David ter Kuile, Noel Jimenez, Oscar, andreacapodacqua, davidterkuile

1.0.4 (2024-04-10)
------------------

1.0.3 (2024-03-26)
------------------
* Add missing realsense simulation dependency
* Contributors: David ter Kuile

1.0.2 (2024-03-26)
------------------

1.0.1 (2024-03-22)
------------------
* Merge branch 'dtk/fix/restructure' into 'humble-devel'
  Dtk/fix/restructure
  See merge request robots/tiago_pro_robot!28
* update copyright year
* Remove unsupported lidars from test
* Add missing realsense2_description dependency
* Add missing robot_state_publisher dependency
* Add missing controller_configuration dependency
* Update supported lasers in urdf
* Add hw_suffix python module for tiago-pro-description
* Add URDF tests
* Restructure URDF
* Choose to spawn the arms or not in the urdf
* Avoid bug that is unable to parse colon with spac ein urdf
* Remove arm meshes
* Merge branch 'dtk/fix/add-hector-gazebo-plugin' into 'humble-devel'
  Add force_based_move gazebo plugin for omni base
  See merge request robots/tiago_pro_robot!27
* Create a pal_distro dependency to not break humble ci untill pr gets accepted
* added hector_gazebo_plugin dep and disabled mobile base controller in simulation
* Add force_based_move gazebo plugin for omni base
* Merge branch 'dtk/fix/camera-simulation' into 'humble-devel'
  Dtk/fix/camera simulation
  See merge request robots/tiago_pro_robot!26
* Add realsense camera in head
* integrate mobile_base_controller
* fix gripper name
* fix on the ft_sensor type
* Contributors: David ter Kuile, andreacapodacqua, davidterkuile, ileniaperrella

1.0.0 (2024-01-30)
------------------
* Merge branch 'ros2-migration' into 'humble-devel'
  Ros2 migration
  See merge request robots/tiago_pro_robot!23
* Fix lintern tests
* remove files not used
* fix misaligned
* fix gripper name
* delete extra choices for the robot_name
* update to 3.8 the cmake_minimum_required Version
* update deg_to_rad file extension
* python module not needed
* update launch files with launch_pal structure
* migration launch files
* urdf migration
* meshes/ rviz config
* CMakeLists and package files
* config files
* migration of CMakeLists.txt and package.xml to ros2
* Contributors: Adria Roig, ileniaperrella

0.0.11 (2023-11-08)
-------------------

0.0.10 (2023-10-20)
-------------------
* Merge branch 'fix/ft_naming' into 'master'
  Change arm_ft\_ to wrist_ft to match TIAGo
  See merge request robots/tiago_pro_robot!19
* Change arm_ft\_ to wrist_ft to match TIAGo
* remove deg_to_rad to make use of pal_urdf_utils package
* Merge branch 'change_name' into 'master'
  Change tiago_v2_prototype to tiago_pro + move arm to an external package
  See merge request robots/tiago_pro_robot!16
* Update package.xml
* Change tiago_v2_prototype to tiago_pro + move arm to an external package
* Contributors: Jordan Palacios, thomaspeyrucain

0.0.9 (2023-05-25)
------------------

0.0.8 (2023-05-24)
------------------
* Merge branch 'wbc_per_arm' into 'master'
  Wbc per arm
  See merge request robots/tiago_pro_robot!10
* Flipped the limits of the head
* Contributors: Sai Kishor Kothakota

0.0.7 (2023-05-24)
------------------

0.0.6 (2023-05-24)
------------------

0.0.5 (2023-05-22)
------------------

0.0.4 (2023-05-20)
------------------
* Merge branch 'flip_arm_link_3' into 'master'
  remove joy_teleop from bringup and use startup as the incrementer server is...
  See merge request robots/tiago_pro_robot!6
* added realsense2_description dependency
* added head_screen_link to the URDF
* Merge branch 'head-camera' into 'flip_arm_link_3'
  Head camera integration
  See merge request robots/tiago_pro_robot!5
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
  See merge request robots/tiago_pro_robot!1
* Added gazebo flags for joint and reformat dynamic parameters for ars, head and torso
* remove log file
* Reduce head joint limits and update dynamic parameters
* Flip joint_2 limits
* Merge branch 'gripper-integration' into 'new_v2_bringup'
  Grippers integration
  See merge request robots/tiago_pro_robot!2
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
