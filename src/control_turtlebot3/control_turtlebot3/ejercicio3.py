#/camera/image_raw [sensor_msgs/msg/Image]
#Topico es : /camera/image_raw 
#Tipo : Image

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge




class SensorLidar(Node):
    
    def __init__(self):
        super().__init__("nodo_acceso_camara")

        #INicializar las variables
        self.imagen = []
        self.bridge = CvBridge()

        #Crear un nodo publicador
        self.publisher = self.create_publisher(Twist, "/cmd_vel",10)
        #Crear un nodo suscriptor
        self.suscriptor = self.create_subscription( Image , "/camera/image_raw" , self.visual_image , 10 )


        self.timer = self.create_timer(0.010, self.visual_image)
        self.get_logger().info("LA camara ha sido iniciada")

    def visual_image(self,msg):
        self.image = msg
        cvImagen = self.bridge.imgmsg_to_cv2(self.image , "bgr8")
        cv2.imshow("ImagenJAime", cvImagen)
        cv2.waitKey()

def main(args = None):
    rclpy.init(args = args)
    nodo = SensorLidar()
    rclpy.spin(nodo)
    rclpy.shutdown()
