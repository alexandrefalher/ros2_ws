#!/usr/bin/python

import datetime

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSDurabilityPolicy, QoSReliabilityPolicy, QoSLivelinessPolicy, QoSHistoryPolicy

from rcl_interfaces.msg import ParameterEvent

from example_interfaces.msg import String

class DummyNode(Node):
    def __init__(self):
        super().__init__("dummy_node")

        qos_profile_parameter_events = QoSProfile(
            reliability=QoSReliabilityPolicy.RMW_QOS_POLICY_RELIABILITY_RELIABLE,
            durability=QoSDurabilityPolicy.RMW_QOS_POLICY_DURABILITY_TRANSIENT_LOCAL,
            liveliness=QoSLivelinessPolicy.AUTOMATIC,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=100
            )
        self._parameter_event_publisher = self.create_publisher(ParameterEvent, "/parameter_events", qos_profile_parameter_events)

        self.declare_parameter("my_param", "something!")
        self.publisher = self.create_publisher(String, "rustdds_topic", 10)
        self.subscription = self.create_subscription(String, "rustdds_topic", self.callback_subscription, 10)
        self.timer = self.create_timer(1, self.publish)
        self.timer_param = self.create_timer(2, self.change_param)
        self.get_logger().info("dummy node initialized")
        self.param_toggle = True
        
    def publish(self):
        msg = String()
        msg.data = "dummy node is publishing !"
        self.publisher.publish(msg)
    
    def callback_subscription(self, msg):
        self.get_logger().info(msg.data)
    
    def change_param(self):
        my_param_value = ""
        if self.param_toggle:
            my_param_value = "True"
            self.param_toggle = False
        else:
            my_param_value = "False"
            self.param_toggle = True
        new_param = rclpy.parameter.Parameter("my_param", rclpy.Parameter.Type.STRING, my_param_value)
        all_new_params = [new_param]
        self.set_parameters(all_new_params)
        self.get_logger().info(f"parameter change: {datetime.datetime.now().time()}")


def main(args=None):
    rclpy.init(args=args)
    node = DummyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
