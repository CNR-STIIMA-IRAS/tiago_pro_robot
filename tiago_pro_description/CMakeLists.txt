cmake_minimum_required(VERSION 3.8)
project(tiago_pro_description)

find_package(ament_cmake_auto REQUIRED)

ament_auto_find_build_dependencies()

if(pal_module_cmake_FOUND)
  pal_register_modules(
    module/20_robot_state_publisher.yaml
  )
elseif(DEFINED ENV{PAL_DISTRO})
  message(FATAL_ERROR "The pal_module_cmake package was not found. Modules not registered.")
endif()


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()

  foreach(wrist_model_right straight-wrist spherical-wrist)
    foreach(wrist_model_left straight-wrist spherical-wrist)
      foreach(end_effector_left pal-pro-gripper no-end-effector)
        foreach(end_effector_right pal-pro-gripper no-end-effector)
          foreach(ft_sensor_left no-ft-sensor rokubi ati)
            foreach(ft_sensor_right no-ft-sensor rokubi ati)
              foreach(tool_changer_left False True)
                foreach(tool_changer_right False True)

                  set(left_side "${wrist_model_left}_tiago-pro_${end_effector_left}_${ft_sensor_left}_${tool_changer_left}")
                  set(right_side "${wrist_model_right}_tiago-pro_${end_effector_right}_${ft_sensor_right}_${tool_changer_right}")

                  add_launch_test(
                    test/test_description.launch.py
                    TARGET "tiago_pro_description_${left_side}_${right_side}"
                    ARGS
                      "arm_type_left:=tiago-pro"
                      "arm_type_right:=tiago-pro"
                      "end_effector_left:=${end_effector_left}"
                      "end_effector_right:=${end_effector_right}"
                      "ft_sensor_left:=${ft_sensor_left}"
                      "ft_sensor_right:=${ft_sensor_right}"
                      "wrist_model_right:=${wrist_model_right}"
                      "wrist_model_left:=${wrist_model_left}"
                      "tool_changer_right:=${tool_changer_right}"
                      "tool_changer_left:=${tool_changer_left}"
                  )

                endforeach()
              endforeach()
            endforeach()
          endforeach()
        endforeach()
      endforeach()
    endforeach()
  endforeach()

  foreach(laser_model no-laser sick-571)
    add_launch_test(
      test/test_description.launch.py
      TARGET "tiago_pro_description_${laser_model}"
      ARGS "laser_model:=${laser_model}"
    )
  endforeach()
endif()

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

ament_auto_package(INSTALL_TO_SHARE config launch robots meshes ros2_control urdf)
