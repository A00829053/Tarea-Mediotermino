# program to capture single image from webcam in python
  
# importing OpenCV library
import cv2
import numpy as np
  
# initialize the camera
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that
cam_port = 0
cam = cv2.VideoCapture(cam_port)
  
# reading the input using the camera
result, image = cam.read()
  
# Resizing the image
image = cv2.resize(image, (700, 600))
  
# Convert Image to Image HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  
# Defining lower and upper bound HSV values
lower = np.array([50, 100, 100])
upper = np.array([70, 255, 255])
  
# Defining mask for detecting color
mask = cv2.inRange(hsv, lower, upper)
  
# Display Image and Mask
cv2.imshow("Image", image)
cv2.imwrite("original.png", image)
cv2.imshow("Mask", mask)
cv2.imwrite("verde.png", mask)

# Make python sleep for unlimited time
cv2.waitKey(0)
