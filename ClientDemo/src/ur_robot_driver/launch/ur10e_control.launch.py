from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # UR robot control node
        Node(
            package='ur_robot_driver',
            executable='ur_control_node',
            name='ur10e_control_node',
            parameters=[{'robot_ip': '127.0.0.1'}],  # Simulated robot IP
            output='screen'
        )
    ])
