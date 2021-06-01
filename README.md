# RECONOCIMIENTO CARA Y OJOS (ROS)

_Se utilizó [OpenCV](https://opencv.org/) para realizar el reconocimiento de cara y ojos dentro de un nodo de ROS._

## FUNCIONAMIENTO
En el nodo [Ojos_cara.py](https://github.com/JuanDBecerra/Reconocimiento_Cara_y_Ojos/blob/main/rco/scripts/Ojos_cara.py) se cargan las librerías de opencv, ROS y otras adicionales, también los archivos que han sido entrenados en reconociento de ojos y cara con anterioridad. La imagen es tomada de la cámara del equipo por medio del package de ROS **usb_cam**, se convierte al formato que OpenCV puede procesar, después a escala de grises que es necesaria para su procesamiento, se hace el reconocimiento y se muestra el resultado sobre la imagen original en tiempo real.

## PRE-REQUISITOS
* [Instalación de OpenCV(4.5.2) en Linux-UBUNTU.](https://docs.opencv.org/4.5.2/d7/d9f/tutorial_linux_install.html)
* Instalación de usb-cam.
```
 $ sudo apt-get install ros-<distro>-usb-cam
````
## EJECUCIÓN
 
* Se corre en un terminal:
```
 $ roscore
```
### Hay dos opciones de ejecutarlo.
  1. Se ejecuta el launch directamente donde se encuentran los nodos que se usan:
  ```
  $ roslaunch rco rco.launch
  ```
  2. Se ejecutan los nodos en diferentes terminales:
  ```
  $ rosrun rco Ojos_cara.py
  ```
  ```
  $ rosrun usb_cam usb_cam_node
  ```
 
