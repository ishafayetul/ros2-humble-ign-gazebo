from launch import LaunchDescription
from launch.actions import ExecuteProcess, LogInfo, SetEnvironmentVariable
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory,get_package_prefix
import os

def generate_launch_description():
    pkg_path_share = get_package_share_directory('robots_description')
    pkg_path_prefix = get_package_prefix('robots_description')
    robot_urdf_path = os.path.join(pkg_path_share, 'models', 'robot_fourW', 'robot_fourW.urdf')
    gz_src_path = pkg_path_prefix+"/share"

    env_var = SetEnvironmentVariable('IGN_GAZEBO_RESOURCE_PATH',gz_src_path)

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_urdf_path
        }]
    )

    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen'
    )

    launch_gz = ExecuteProcess(
        cmd=['ign', 'gazebo', '-r','empty.sdf'],
        output='screen'
    )

    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        parameters=[{'use_sim_time': True}],
        arguments=['-name', 'robot_fourW', 
                   '-file', robot_urdf_path,
                   '-x','0', 
                   '-y','0',
                   '-z','-0.065'],
        output='screen'
    )
    
    
    return LaunchDescription([
        LogInfo(msg=pkg_path_share),
        LogInfo(msg=pkg_path_prefix),
        LogInfo(msg=robot_urdf_path),
        LogInfo(msg=gz_src_path),
        #LogInfo(msg=robot_urdf),
        env_var,
        # robot_state_publisher,
        # joint_state_publisher,
        launch_gz,
        spawn_robot,
        
    ])
