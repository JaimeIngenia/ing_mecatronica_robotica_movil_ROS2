import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):

        super().__init__("py_test")
        self.counter = 0
        self.get_logger().info("Hola HOla Jaime")
        self.create_timer(2, self.timmer_llamando)

    def timmer_llamando(self):
        self.counter = self.counter +1
        self.get_logger().info("Hello" + str(self.counter))


def main(args=None):
    rclpy.init(args=args)
    #node = Node("py_test")
    node = MyNode()
    #node.get_logger().info("Hello ROS2 jaime")
    rclpy.spin(node) #Este linea permite la comunicacion entre nodos
    rclpy.shutdown()

if __name__ == "__main__":
    main()






# def main(args=None):
#     rclpy.init(args=args)
#     node = Node("py_test")
#     node.get_logger().info("Hello ROS2 jaime")
#     rclpy.spin(node) #Este linea permite la comunicacion entre nodos
#     rclpy.shutdown()

# if __name__ == "__main__":
#     main()



