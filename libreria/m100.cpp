#include <iostream>
#include <stdio.h>

bool multiplicacion(double* val_in, int val_in_size) {
   for (int i=0; i < val_in_size; i++) {
      std::cout << val_in[i] << std::endl;
      val_in[i] = val_in[i]*100;
   }      
   return true;
}
