from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    bridge_node = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='ros_gz_bridge',
        output='screen',
        parameters=[{'use_sim_time': True}],
        arguments=[
            '/model/robot_fourW/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist',
            '/model/robot_fourW/odometry@nav_msgs/msg/Odometry@ignition.msgs.Odometry',
            '/model/robot_fourW/tf@tf2_msgs/msg/TFMessage@ignition.msgs.Pose_V',
            "/clock@rosgraph_msgs/msg/Clock@ignition.msgs.Clock",
        ],
        remappings=[
            ('/model/robot_fourW/cmd_vel', '/cmd_vel'),
            ('/model/robot_fourW/odometry', '/odometry'),
            ('/model/robot_fourW/tf', '/tf'),
        ]
    )
    return LaunchDescription([
        bridge_node,
    ])