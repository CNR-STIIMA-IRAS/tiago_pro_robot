cmake_minimum_required(VERSION 3.8)
project(tiago_pro_description)

find_package(ament_cmake_auto REQUIRED)

ament_auto_find_build_dependencies()

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()

  foreach(arm_type_left tiago-pro no-arm)
    foreach(arm_type_right tiago-pro no-arm)
        foreach(end_effector_left pal-pro-gripper custom no-end-effector)
            foreach(end_effector_right pal-pro-gripper custom no-end-effector)
                foreach(ft_sensor_left no-ft-sensor rokubi)
                    foreach(ft_sensor_right no-ft-sensor rokubi)

                        set(left_side "${arm_type_left}_${end_effector_left}_${ft_sensor_left}")
                        set(right_side "${arm_type_right}_${end_effector_right}_${ft_sensor_right}")

                        add_launch_test(
                          test/test_description.launch.py
                          TARGET "tiago_pro_description_${left_side}_${right_side}"
                          ARGS
                          "arm_type_left:=${arm_type_left}"
                          "arm_type_right:=${arm_type_right}"
                          "end_effector_left:=${end_effector_left}"
                          "end_effector_right:=${end_effector_right}"
                          "ft_sensor_left:=${ft_sensor_left}"
                          "ft_sensor_right:=${ft_sensor_right}"
                        )
                    endforeach()
                endforeach()
            endforeach()
        endforeach()
      endforeach()
    endforeach()
  foreach(laser_model no-laser sick-551 sick-561 sick-571 hokuyo)
    add_launch_test(
      test/test_description.launch.py
      TARGET "tiago_pro_description_${laser_model}"
      ARGS "laser_model:=${laser_model}"
    )
  endforeach()
endif()

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

ament_auto_package(INSTALL_TO_SHARE config launch gazebo robots meshes ros2_control urdf)
