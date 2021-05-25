#!/usr/bin/env python   # Para asegura que la línea de comandos se ejecute como una secuencia de comandos de Python

# Se importan librerías
import rospy
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge, CvBridgeError
import cv2 
import sys

# Ubicación donde esta el archivo que ha sido entrenado con anterioridad para el reconocimimeto de cara
face_cascade = cv2.CascadeClassifier('/home/juan-david/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')
# Mensaje si no se encuentra la ruta
if face_cascade.empty(): raise Exception("¿Está seguro que es la ruta correcta?") 
# Ubicación donde esta el archivo que ha sido entrenado con anterioridad para el reconocimimeto de ojos
eye_cascade = cv2.CascadeClassifier('/home/juan-david/opencv-master/data/haarcascades/haarcascade_lefteye_2splits.xml')
if eye_cascade.empty(): raise Exception("¿Está seguro que es la ruta correcta?")

# Clase para procesar la imagen
class image_converter:
    # Método constructor
    def __init__(self):
        self.image_pub = rospy.Publisher("Image_pub", Image)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/usb_cam/image_raw",Image,self.callback)
    
    # Método destructor
    def __del__(self):
        cv2.destroyAllWindows()

    def callback(self,data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data,"bgr8")  # Convierte la imagen recida en ROS a una imagen que se puede usar en OpenCV
        except CvBridgeError as e:
            print(e)
        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY) # Convierte la imagen a escala de grises
        faces = face_cascade.detectMultiScale(gray, 1.5,  5) # Detecta la cara
        for (x, y, w, h) in faces:
            cv2.putText(cv_image,'Face',(15,15),5,1,(255,0,0),1,cv2.LINE_AA) # Escribe "Face" en la esquina superior izquierda
            cv2.rectangle(cv_image,(x, y), (x + w, y + h), (255, 0, 0), 2) # Resalta la cara encontrada

        eyes = eye_cascade.detectMultiScale(gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.putText(cv_image,'Eyes',(15,30),5,1,(0,0,255),1)    # Escribe "Eyes" en la esquina superior izquierda
            cv2.rectangle(cv_image, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)  # Resalta los ojos resaltados
        cv2.imshow("Image", cv_image) # Muestra el video
        cv2.waitKey(3)  # Delay 
        try:
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
        except CvBridgeError as e:
            print(e)

def main(args):
  ic = image_converter()
  rospy.init_node('rco', anonymous=False)
  rospy.spin()
if __name__ == '__main__':
    main(sys.argv)
  