import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Get the path to the SDF file
    robot_gazebo_dir = get_package_share_directory('robot_gazebo')
    sdf_file_path = os.path.join(robot_gazebo_dir, 'sdf', 'robot.sdf')

    # Declare the launch arguments
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    # Gazebo launch file
    gazebo_launch_file_dir = os.path.join(get_package_share_directory('gazebo_ros'), 'launch')
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(gazebo_launch_file_dir, 'gazebo.launch.py')),
        launch_arguments={'world': sdf_file_path}.items(),
    )

    # Return the launch description
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true'
        ),
        gazebo_launch,
    ])