#/cmd_vel [geometry_msg/msg/Twist]
#Topico es : /cmd_vel
#Tipo : Twist

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist



class Publisher(Node):
    
    def __init__(self):
        super().__init__("nodo_publicador")

        #INicializar las variables
        self.velocidad_lineal =2.0
        self.velocidad_angular =1.0
        #Crear un nodo publicador
        self.publisher = self.create_publisher(Twist, "/cmd_vel",10)
        self.timer = self.create_timer(0.01, self.publicar_velocidades)
        self.get_logger().info("Estamos publicando velocidades")

    def publicar_velocidades(self):
        vel = Twist()
        vel.linear.x = 2.0#self.velocidad_lineal
        vel.angular.z = 1.0#self.velocidad_angular
        self.publisher.publish(vel)

def main(args = None):
    rclpy.init(args = args)
    nodo = Publisher()
    rclpy.spin(nodo)
    rclpy.shutdown()
