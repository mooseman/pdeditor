

/*  len.c  */  

/*  Length of an array  */ 


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>


/* Length of an array */ 
int len(char *arrname, char *type) 
{ 
  return sizeof(arrname) / sizeof(type);          
}     


int len2(char *arrname) 
{ 
  return sizeof(arrname) / sizeof(char); 
}     


char myarray[] = "foobarbaz" ;  


int main() 
{ 

  printf("Length is %d \n", len(myarray, "char") );  
  
  printf("Length is %d \n", len2(myarray) );  


return 0; 

} 










