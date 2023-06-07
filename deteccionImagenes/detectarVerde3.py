import cap
import numpy as np
import cv2
import ctypes


# Capturing video through webcam
webcam = cv2.VideoCapture(0)
# Load the C library
lib = ctypes.CDLL('./m100_2.so')
# Define the C function argument and return types
lib.multiply_array.argtypes = (ctypes.POINTER(ctypes.c_double), ctypes.c_int)
lib.multiply_array.restype = ctypes.POINTER(ctypes.c_double)
while (1):
    
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
        x,y,w,h = cv2.boundingRect(c)
        # draw the biggest contour (c) in green
        cv2.rectangle(imageFrame,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.putText(imageFrame, "Center: (" + str(x) + ", " + str(y) + ")", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0, (0, 255, 0))

    array = np.array([x,y], dtype=np.float64)
    # Call the C function with the array
    c_arr = array.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    c_result = lib.multiply_array(c_arr, len(array))

    # Convert the result back to a Python array
    result = np.ctypeslib.as_array(c_result, shape=(len(array),))
    print(result)
    # Program Termination
    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
