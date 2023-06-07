import ctypes as cty
import pathlib
import numpy as np

if __name__ == "__main__":
    # Load the shared library into ctypes
    libname = "m100.so"
    c_lib = cty.CDLL(libname)
    val_in = np.array([1,2])
    print(val_in)
    c_val_in = (cty.c_int * len(val_in))(*val_in)
    val_out = np.array([0,0])
    c_val_out = (cty.c_int * len(val_out))(*val_out)
    answer = c_lib.multiplicacion(c_val_in, 2, c_val_out, 2)
    print(answer)
    print(c_val_out)