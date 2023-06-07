import ctypes
import numpy as np

# Load the C library
lib = ctypes.CDLL('/Users/TecMonterrey/Downloads/Tarea Mediotermino/libreria/try2/m100_2.so')  # Replace with the path to your compiled shared library

# Define the C function argument and return types
lib.multiply_array.argtypes = (ctypes.POINTER(ctypes.c_double), ctypes.c_int)
lib.multiply_array.restype = ctypes.POINTER(ctypes.c_double)

# Create a double array in Python
arr = np.array([1.0, 2.5, 3.7, 4.2, 5.9], dtype=np.float64)

# Call the C function with the array
c_arr = arr.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
c_result = lib.multiply_array(c_arr, len(arr))

# Convert the result back to a Python array
result = np.ctypeslib.as_array(c_result, shape=(len(arr),))

# Print the result
print(result)
