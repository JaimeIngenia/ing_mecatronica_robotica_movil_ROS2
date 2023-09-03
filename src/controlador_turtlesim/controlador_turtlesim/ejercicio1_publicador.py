#Dentro del archivo "ejercicio1_publicador" programar el sigueinte codigo

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Publisher(Node):
    
    def __init__(self):
        super().__init__("nodo_publicador")
        self.publisher = self.create_publisher(Twist, "/turtle1/cmd_vel",10)
        self.timer = self.create_timer(0.5, self.publicar_velocidades)
        self.get_logger().info("EL nodo ha empezado a publicar mensajes")

    def publicar_velocidades(self):
        vel = Twist()
        vel.linear.x = 2.0
        vel.angular.z = 1.0
        self.publisher.publish(vel)

def main(args = None):
    rclpy.init(args = args)
    nodo = Publisher()
    rclpy.spin(nodo)
    rclpy.shutdown()


