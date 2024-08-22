^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_pro_bringup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.4.0 (2024-08-22)
------------------
* Adapted so it is the same as tiago dual
* Suggested changes
* Added play motion module
* Suggested changes
* Hardware specific motions with grippers
* Contributors: oscarmartinez

1.3.0 (2024-08-08)
------------------

1.2.0 (2024-08-07)
------------------

1.1.0 (2024-08-05)
------------------
* enabled y-axis base movements
* Fix path
* Fix default device
* Contributors: andreacapodacqua, thomas.peyrucain

1.0.13 (2024-07-09)
-------------------
* Add warning for pal_module_cmake not found
* Contributors: Noel Jimenez

1.0.12 (2024-06-27)
-------------------

1.0.11 (2024-06-26)
-------------------
* Merge branch 'dtk/move-robot-args' into 'humble-devel'
  Change import for launch args
  See merge request robots/tiago_pro_robot!50
* Change import for launch args
* Merge branch 'dtk/fix/joystick-driver' into 'humble-devel'
  Add new joy_linux node
  See merge request robots/tiago_pro_robot!45
* Add joy linux to launch file
* Add new joy_linux node
* Contributors: David ter Kuile, davidterkuile

1.0.10 (2024-05-22)
-------------------

1.0.9 (2024-05-09)
------------------

1.0.8 (2024-04-26)
------------------

1.0.7 (2024-04-18)
------------------
* Merge branch 'dtk/fix/play-motion2-dependency' into 'humble-devel'
  Add dependency of play_motion2
  See merge request robots/tiago_pro_robot!37
* Add dependency of play_motion2
* Merge branch 'omm/feat/public_sim_check' into 'humble-devel'
  Public Sim check
  See merge request robots/tiago_pro_robot!36
* is_public_sim support in launch files
* Contributors: Oscar, davidterkuile

1.0.6 (2024-04-17)
------------------

1.0.5 (2024-04-16)
------------------
* Merge branch 'dtk/feat/add-modules' into 'humble-devel'
  Dtk/feat/add modules
  See merge request robots/tiago_pro_robot!32
* fix teleop config file paths and names
* Fix argument typo in joy_teleop
* Add modules
* Contributors: David ter Kuile, Noel Jimenez

1.0.4 (2024-04-10)
------------------

1.0.3 (2024-03-26)
------------------

1.0.2 (2024-03-26)
------------------
* Merge branch 'dtk/fix/fix-nav-topic' into 'humble-devel'
  Dtk/fix/fix nav topic
  See merge request robots/tiago_pro_robot!29
* Change twist mux navigation topic
* Add missing sim time to twist mux
* Contributors: David ter Kuile, andreacapodacqua

1.0.1 (2024-03-22)
------------------
* Merge branch 'dtk/fix/restructure' into 'humble-devel'
  Dtk/fix/restructure
  See merge request robots/tiago_pro_robot!28
* update copyright year
* Add missnig use sim time arg
* Update motion name
* Disable gripper specific motions
* update config files
* Add regen_em script
* Restructure launch file tiago_pro_bringup
* Merge branch 'fix/rename_approach_planner' into 'humble-devel'
  Rename approach_planner config to motion_planner
  See merge request robots/tiago_pro_robot!25
* Rename approach_planner config to motion_planner
* Merge branch 'fix/update_approach_planner_config' into 'humble-devel'
  Update approach_planner configuration
  See merge request robots/tiago_pro_robot!24
* Update approach_planner configuration
* Contributors: David ter Kuile, Jordan Palacios, Noel Jimenez, davidterkuile

1.0.0 (2024-01-30)
------------------
* Merge branch 'ros2-migration' into 'humble-devel'
  Ros2 migration
  See merge request robots/tiago_pro_robot!23
* fix twist_mux config name
* simplify joy_telop launch file (as done for tiago and ari)
* update to 3.8 the cmake_minimum_required Version
* twist mux and joytelop added - to check
* update launch files with launch_pal structure
* update motions yaml file
* migration launch files
* CMakeLists and package files
* config files
* migration of CMakeLists.txt and package.xml to ros2
* Contributors: Adria Roig, ileniaperrella

0.0.11 (2023-11-08)
-------------------

0.0.10 (2023-10-20)
-------------------
* Merge branch 'change_name' into 'master'
  Change tiago_v2_prototype to tiago_pro + move arm to an external package
  See merge request robots/tiago_pro_robot!16
* Change tiago_v2_prototype to tiago_pro + move arm to an external package
* Contributors: Jordan Palacios, thomaspeyrucain

0.0.9 (2023-05-25)
------------------
* Merge branch 'fix_home' into 'master'
  new home gripper 7
  See merge request robots/tiago_pro_robot!11
* no alive motions
* new home gripper 7
* Contributors: Aina, Sai Kishor Kothakota

0.0.8 (2023-05-24)
------------------
* Merge branch 'wbc_per_arm' into 'master'
  Wbc per arm
  See merge request robots/tiago_pro_robot!10
* added the motion tiago_dancing_happy
* Contributors: Sai Kishor Kothakota

0.0.7 (2023-05-24)
------------------

0.0.6 (2023-05-24)
------------------
* Merge branch 'fix_motions' into 'master'
  Fix motions
  See merge request robots/tiago_pro_robot!7
* modified home motion so the arms won't need to support on base covers on poweroff
* new home_right/left and gripper fixed on tiago_dancing
* no meta descriptio
* alie_fixed and home joint 7
* offer and shake
* Contributors: Aina, Sai Kishor Kothakota

0.0.5 (2023-05-22)
------------------

0.0.4 (2023-05-20)
------------------
* Merge branch 'flip_arm_link_3' into 'master'
  remove joy_teleop from bringup and use startup as the incrementer server is...
  See merge request robots/tiago_pro_robot!6
* added the new home motion and review the torso heights
* fix up the main motions for stress testing
* Don't start actuator pid controllers and position controllers by default, and handle it by an application
* remove joy_teleop from bringup and use startup as the incrementer server is timing out with delay in deployer
* comment out the robot pose publisher until the navigation is setup
* added more motions generated by aina
* launch Move group for motion planning
* load the pre-defined motions in the play_motion launch file
* added some generic motion configuration on the TIAGo2 Robot
* Contributors: Sai Kishor Kothakota

0.0.3 (2023-05-16)
------------------
* Merge branch 'play_motion_fixes' into 'master'
  play motion fixes
  See merge request robots/tiago_pro_robot!4
* add play_motion to the bringup launch
* added head joints in the exclude from planning joints list
* Contributors: Sai Kishor Kothakota, ileniaperrella

0.0.2 (2023-05-16)
------------------

0.0.1 (2023-05-16)
------------------
* Merge branch 'new_v2_bringup' into 'master'
  New v2 bringup and urdf
  See merge request robots/tiago_pro_robot!1
* Merge branch 'play-motion' into 'new_v2_bringup'
  Play motion
  See merge request robots/tiago_pro_robot!3
* update the actuator PID values for the whole arm
* added play_motion launch files
* Launch actuator pid controller and load its configuration
* Fix broken path
* added the bringup package and the configuration
* Contributors: Jordan Palacios, Sai Kishor Kothakota, ileniaperrella
