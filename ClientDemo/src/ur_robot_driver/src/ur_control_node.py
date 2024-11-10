import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class URControlNode(Node):
    def __init__(self):
        super().__init__('ur_control_node')
        self.publisher = self.create_publisher(String, 'ur10e/command', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Simulating UR10e robot movement'
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = URControlNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
