from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_path_share = get_package_share_directory('robots_description')
    robot_xacro_path = os.path.join(pkg_path_share, 'models', 'robot_fourW', 'robot_fourW.urdf.xacro')

    robot_urdf = Command(['xacro ', robot_xacro_path])
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_urdf
        }]
    )
    joint_state_publisher = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )
    rviz_node=Node(
        name="rviz2",
        package="rviz2",
        executable="rviz2",
        output="screen",
        parameters=[{'use_sim_time': True}],
        arguments=["-d", os.path.join(pkg_path_share,"rviz","display.rviz")]
        
    )
    return LaunchDescription([
        robot_state_publisher,
        joint_state_publisher,
        rviz_node,
    ])
