#include "m100_2.h"
#include <stdio.h>
#include <stdlib.h>

double* multiply_array(double* arr, int length) {
    double* result = (double*)malloc(length * sizeof(double));
    for (int i = 0; i < length; i++) {
        result[i] = arr[i] * 100.0;
    }
    return result;
}