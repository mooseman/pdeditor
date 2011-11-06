

/*  gapbuffer.c                                 */  
/*  A simple gapbuffer implementation.          */ 
/*  This code is released to the public domain. */  
/*  "Share and enjoy..."  ;)                    */


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <malloc.h>  


char *slice(char *array, int first, int last) 
{ 
    char *retarray = (char*) malloc(last-first);         
                       
    /*  Do the array slice  */          
    strncpy(retarray, array+first, last);
     
    return retarray;                      
    free(retarray);  
    retarray = NULL;                                                                    
}  


/*  Return the current contents of the text variable */ 
char *fulltext(void) 
{  
   return fulltext;      
}      


/*  Return the first text buffer */ 
char *buffer1(void) 
{ 
   char *retbuf = slice(fulltext, 0, pos);
   return retbuf;    
}     


/*  Return the second text buffer */ 
char *buffer2(void) 
{ 
   char *retbuf = slice(fulltext, pos, strlen(fulltext) );
   return retbuf;    
}     







    /** Unit testing. **/
int main() 
{ 
    
  char *fulltext = "Mary had a little lamb, its fleece was white as snow."; 
    
  
  
        
return 0; 
        
}




    



