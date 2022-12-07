cmake_minimum_required(VERSION 2.8.3)
project(tiago_v2_prototype_description)

find_package(catkin REQUIRED)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES tiago_v2_prototype_description
#  CATKIN_DEPENDS joint_state_publisher_gui tiago_sea_arm_description xacro
#  DEPENDS system_lib
)

foreach(dir config meshes robots urdf)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
