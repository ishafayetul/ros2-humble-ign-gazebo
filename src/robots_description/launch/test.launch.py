from launch import LaunchDescription
from launch.actions import ExecuteProcess, LogInfo, SetEnvironmentVariable
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_path = get_package_share_directory('robots_description')
    robot_xacro_path = os.path.join(pkg_path, 'models', 'robot_fourW', 'robot_fourW.xacro')
    gz_src_path = os.path.join(pkg_path, 'models', 'robot_fourW')

    # Set GAZEBO_MODEL_PATH
    env_var = SetEnvironmentVariable(
        'GAZEBO_MODEL_PATH',
        gz_src_path
    )

    # Process the xacro
    robot_urdf = Command(
        ['xacro ', robot_xacro_path]
    )

    # Launch Gazebo (Classic)
    gz_world = ExecuteProcess(
        cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
        output='screen',
    )

    # Spawn the robot into Gazebo
    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spawn_robot',
        output='screen',
        arguments=[
            '-entity', 'robot_fourW',
            '-topic', 'robot_description',
        ]
    )

    # State publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_urdf}]
    )

    # Joint state publisher
    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen'
    )

    return LaunchDescription([
        LogInfo(msg='---------- Setting GAZEBO_MODEL_PATH ----------'),
        env_var,

        LogInfo(msg='---------- Starting Robot State Publisher ----------'),
        robot_state_publisher,

        LogInfo(msg='---------- Starting Joint State Publisher ----------'),
        joint_state_publisher,

        LogInfo(msg='---------- Launching Gazebo ----------'),
        gz_world,

        LogInfo(msg='---------- Spawning robot_fourW into simulation ----------'),
        spawn_robot,
    ])
