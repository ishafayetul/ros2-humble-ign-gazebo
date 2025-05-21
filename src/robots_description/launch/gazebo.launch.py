from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_dir = get_package_share_directory('robots_description')
    urdf_path = os.path.join(pkg_dir, 'models','robot_fourW', 'robot_fourW.urdf')

    return LaunchDescription([
        # 1. Launch Ignition Gazebo with a world
        ExecuteProcess(
            cmd=['ign', 'gazebo', '-v','4', '-r','empty.sdf'],
            output='screen'
        ),
        # 3. Use xacro to convert and publish robot description
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': open(urdf_path).read()
            }]
        ),

        # 4. Spawn robot in Ignition
        Node(
        package='ros_ign_gazebo',
        executable='create',
        name='spawn_robot',
        output='screen',
        arguments=[
            '-name', 'robot_fourW',
            '-file', urdf_path,
            '-x', '0', '-y', '0', '-z', '0'
            ]
        ),
    ])
