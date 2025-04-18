from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_path = get_package_share_directory('assembly_1_robot_arm')
    urdf_path = os.path.join(pkg_path, 'urdf', 'assembly_1_robot_arm.urdf')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'assembly_1_robot_arm',
                '-file', urdf_path
            ],
            output='screen'
        )
    ])
