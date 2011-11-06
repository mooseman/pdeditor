

/*  slice.c  */ 

/*  Get a slice from an array  */  



#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h> 
#include <ctype.h>


char *slice(char *arrname, int start, int end) 
{ 
   /* An array to hold the slice */  
   char retarray[end-start];  
   
   int i; 
   
   for(i=start;i<end;i++) 
   { 
      strcat(retarray, (char)arrname[i]);  
      
   }  
   
   return retarray;     
  
} 


char *myarray[] = "Mary had a little lamb"; 


int main() 
{ 

  printf("Slice is %s \n", slice(myarray, 5, 11) ); 

  return 0; 

} 


 








