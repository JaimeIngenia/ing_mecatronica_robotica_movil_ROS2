
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class Suscriber(Node):

    def __init__(self):
        super().__init__("nodo_suscriptor")
        self.suscriptor = self.create_subscription(Pose,"/turtle1/pose",self.publicar_posiciones,10) 

    def publicar_posiciones(self, msg:Pose):
        self.get_logger().info(str(msg))

def main(args = None):
    rclpy.init(args = args)
    nodo = Suscriber()
    rclpy.spin(nodo)
    rclpy.shutdown()