#!/usr/bin/python

import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class DummyNode(Node):
    def __init__(self):
        super().__init__("dummy_node")
        self.publisher = self.create_publisher(String, "dummy_node__pub", 10)
        self.subscription = self.create_subscription(String, "dummy_node__sub", self.callback_subscription, 10)
        self.timer = self.create_timer(1, self.publish)
        self.get_logger().info("dummy node initialized")
    
    def publish(self):
        msg = String()
        msg.data = "dummy node is publishing !"
        self.publisher.publish(msg)
    
    def callback_subscription(self, msg):
        self.get_logger().info(msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = DummyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
