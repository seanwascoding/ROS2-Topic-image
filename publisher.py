# coding=UTF-8 
import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String 
import cv2
import time
import base64
import os

class Ex3_pub(Node): 
    def __init__(self):
    	# init 
        super().__init__('Ex3_pub')
        self.publisher_ = self.create_publisher(String, 'Image', 10) 
        
	# images
        self.counter = 0
        self.image_folder = './stone/'
        self.image_files = sorted([os.path.join(self.image_folder, img) for img in os.listdir(self.image_folder) if img.endswith(".jpg") | img.endswith(".bmp") | img.endswith(".png")])
        print('images:', len(self.image_files))
        
        # timer
        self.timer = self.create_timer(0.1, self.timer_callback) 

    def timer_callback(self): 
        msg = String() 
        img = cv2.imread(self.image_files[self.counter])
        if(self.counter == len(self.image_files)-1):
                self.counter = 0
        else:
        	self.counter += 1
        msg.data = base64.b64encode(cv2.imencode('.png', img)[1].tobytes()).decode('utf-8')
        self.publisher_.publish(msg)

if __name__ == '__main__': 
    rclpy.init() 
    ex3_publisher = Ex3_pub() 
    rclpy.spin(ex3_publisher) 
    ex3_publisher.destroy_node()
    rclpy.shutdown()
