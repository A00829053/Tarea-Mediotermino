#!/usr/bin/env python

import cap
import numpy as np
import cv2
import rospy
import ctypes
from std_msgs.msg import Float64MultiArray

def publish_coordinates():
    # Initialize the ROS node
    rospy.init_node('coords_pub', anonymous=True)

    # Create a publisher for the coordinates topic
    coordinates_pub = rospy.Publisher('coordinates', Float64MultiArray, queue_size=10)

    rate = rospy.Rate(10)  # Publish coordinates at 10Hz
    # Capturing video through webcam
    webcam = cv2.VideoCapture(0)
    # Load the C library
    lib = ctypes.CDLL('./m100_2.so')
    # Define the C function argument and return types
    lib.multiply_array.argtypes = (ctypes.POINTER(ctypes.c_double), ctypes.c_int)
    lib.multiply_array.restype = ctypes.POINTER(ctypes.c_double)

    while not rospy.is_shutdown():
        x = 0.0
        y = 0.0
        _, imageFrame = webcam.read()

        # Convert the imageFrame in
        # BGR(RGB color space) to
        # HSV(hue-saturation-value)
        # color space
        hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

        # Set range for green color and
        # define mask
        green_lower = np.array([25, 52, 72], np.uint8)
        green_upper = np.array([102, 255, 255], np.uint8)
        green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

        # Morphological Transform, Dilation
        # for each color and bitwise_and operator
        # between imageFrame and mask determines
        # to detect only that particular color
        kernal = np.ones((5, 5), "uint8")

        # For green color
        green_mask = cv2.dilate(green_mask, kernal)

        # Creating contour to track green color
        contours, _ = cv2.findContours(green_mask,
                                            cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
        # find the biggest countour (c) by the area
        if len(contours) > 0:
            c = max(contours, key = cv2.contourArea)
            # FINAL 1
            x,y,_,_ = cv2.boundingRect(c)

        array = np.array([x,y], dtype=np.float64)
        # Call the C function with the array
        c_arr = array.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
        c_result = lib.multiply_array(c_arr, len(arr))

        # Convert the result back to a Python array
        result = np.ctypeslib.as_array(c_result, shape=(len(array),))
        
        # Update the x and y coordinates
        coords = Float64MultiArray()
        coords.data = result

        # Publish the coordinates
        coordinates_pub.publish(coords)

        rate.sleep()

if __name__ == '__main__':
    try:
        publish_coordinates()
    except rospy.ROSInterruptException:
        pass