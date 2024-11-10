from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        # Declare robot IP argument for simulation (use localhost or leave it empty for simulation)
        DeclareLaunchArgument('robot_ip', default_value='127.0.0.1', description='Robot IP address'),

        # Gazebo simulation environment (Start Gazebo with the robot model)
        Node(
            package='gazebo_ros',
            executable='gzserver',
            name='gazebo_server',
            output='screen',
            parameters=[{'robot_ip': LaunchConfiguration('robot_ip')}],
            arguments=['-s', 'libgazebo_ros_factory.so']
        ),

        Node(
            package='gazebo_ros',
            executable='gzclient',
            name='gazebo_client',
            output='screen'
        ),

        # UR robot driver (this will simulate robot control)
        Node(
            package='ur_robot_driver',
            executable='ur_control_node',
            name='ur10e_control',
            parameters=[{'robot_ip': '127.0.0.1'}],  # Simulated IP address
            output='screen'
        ),

        # Robot description for Gazebo
        Node(
            package='ur_description',
            executable='urdf_to_gazebo',
            name='ur10e_urdf',
            output='screen',
            parameters=[{'robot_ip': '127.0.0.1'}]  # Simulated IP address
        ),

        # Joint state publisher for controlling robot joints in Gazebo
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher',
            output='screen'
        )
    ])
