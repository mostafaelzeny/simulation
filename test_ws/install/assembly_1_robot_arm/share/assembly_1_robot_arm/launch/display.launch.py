from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Get the package path
    pkg_path = get_package_share_directory('assembly_1_robot_arm')
    
    # Define paths for URDF and RViz config
    urdf_path = os.path.join(pkg_path, 'urdf', 'assembly_1_robot_arm.urdf')
    rviz_config_path = os.path.join('/home/mo/test_ws/src/assembly_1_robot_arm/', 'rviz', 'config.rviz')

    # Check if URDF file exists
    if not os.path.exists(urdf_path):
        raise FileNotFoundError(f"URDF file not found: {urdf_path}")

    # Check if RViz config file exists (optional)
    if not os.path.exists(rviz_config_path):
        print(f"Warning: RViz config file not found: {rviz_config_path}. RViz will open with default settings.")

    # Launch description
    return LaunchDescription([
        # Robot State Publisher Node
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_path).read()}]
        ),
        # Joint State Publisher GUI Node
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),
        # RViz Node
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path] if os.path.exists(rviz_config_path) else []
        )
    ])
