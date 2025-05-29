from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_path_share = get_package_share_directory('robots_description')
    #robot_xacro_path = os.path.join(pkg_path_share, 'models', 'robot_fourW', 'robot_fourW.urdf')

    rviz_node=Node(
        name="rviz2",
        package="rviz2",
        executable="rviz2",
        output="screen",
        parameters=[{'use_sim_time': True}],
        arguments=["-d", os.path.join(pkg_path_share,"rviz","display.rviz")]
        
    )
    return LaunchDescription([
        rviz_node,
    ])
