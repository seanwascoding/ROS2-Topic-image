# coding=UTF-8 
import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String 
import cv2
import base64
import numpy as np

class Ex3_sub(Node): 
    def __init__(self): 
        
        super().__init__('Ex3_sub') 
        self.subscription = self.create_subscription(String,"Image",self.listener_callback,10) 
        self.subscription #prevent unused variable warning 

    def listener_callback(self, msg): 
        cv2.namedWindow("Image Stream", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Image Stream", 416, 416)
        self.get_logger().info('Get the image')
        img_base64 = msg.data
        img_bytes = base64.b64decode(img_base64)
        img_np = np.frombuffer(img_bytes, dtype=np.uint8)
        img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)  
        cv2.imshow('Image Stream', img)
        cv2.waitKey(1)

if __name__ == '__main__': 
    rclpy.init() 
    ex3_subscriber = Ex3_sub() 
    rclpy.spin(ex3_subscriber) 
    ex3_subscriber.destroy_node() 
    cv2.destroyAllWindows()
    rclpy.shutdown()
