#/scan [sensor_msgs/msg/LaserScan]
#Topico es : /scan
#Tipo : LaserScan

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan



class SensorLidar(Node):
    
    def __init__(self):
        super().__init__("nodo_turtleScan")

        #INicializar las variables
        self.rangos = []
        self.velocidad_lineal = 0.5
        self.velocidad_angular = 0.0
        self.estado_inicial_sensor = False

        #Crear un nodo publicador
        self.publisher = self.create_publisher(Twist, "/cmd_vel",10)
        #Crear un nodo suscriptor
        self.suscriptor = self.create_subscription( LaserScan , "/scan" , self.sensor , 10 )


        self.timer = self.create_timer(0.010, self.actualizacion_estado)
        self.get_logger().info("Estamos publicando velocidades")

    def sensor(self,msg):
        self.rangos = msg.ranges
        self.estado_inicial_sensor = True

    def actualizacion_estado(self):  
        if self.estado_inicial_sensor is True:
            self.controlVel()
    def controlVel(self):
        vel = Twist()
        if self.rangos[0] < 1:
            vel.linear.x = 0.0
            vel.angular.z = -0.5
        else:
            vel.linear.x = self.velocidad_lineal
            vel.angular.z = self.velocidad_angular
        self.publisher.publish(vel)

def main(args = None):
    rclpy.init(args = args)
    nodo = SensorLidar()
    rclpy.spin(nodo)
    rclpy.shutdown()