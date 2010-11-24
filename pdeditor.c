

/*  pdeditor.c                                   */  
/*  A simple text-editor in C                    */ 
/*  This code is released to the public domain.  */ 
/*  "Share and enjoy..."  ;)                     */ 


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <curses.h>


/* Declare our window  */ 
   WINDOW *mywin;  

/* Number of rows and cols */ 
int r, c, nrows, ncols;  

/*  Character read from keyboard. */ 
/*  Note - make sure this is an INT variable. */ 
int ch; 


/* Move to the beginning of the next line */ 
void nextline() 
{ 
   move(r+1, 0); 
   getyx(mywin, r, c);
   refresh();     
}     

void delchar() 
{    
   delch();   
   refresh();             
}     



void up()
{
  getyx(mywin, r, c);
  move(r-1, c);     
  refresh();                  
} 


void down()
{
  getyx(mywin, r, c);
  move(r+1, c);     
  refresh();                  
} 


void right()
{
  getyx(mywin, r, c);
  move(r, c+1);     
  refresh();                      
} 


void left() 
{
  getyx(mywin, r, c);
  move(r, c-1);     
  refresh();            
} 


void backspace()
{   
  getyx(mywin, r, c);
  move(r, c-1);   
  delch();   
  refresh();       
}     
    


/*  Handle the keyboard input  */ 
void keyhandler() 
{ 
  
  getyx(mywin, r, c);
  /*  Handle input here */    
  ch = getch();   
  if (ch == KEY_BACKSPACE)    backspace();  
  else if (ch == KEY_DC)      delch(); 
  else if (ch == KEY_LEFT)    left(); 
  else if (ch == KEY_RIGHT)   right(); 
  else if (ch == KEY_UP)      up();
  else if (ch == KEY_DOWN)    down();    
  else addch(ch); 
                        
}     




int main(int argc, char *argv[])
{    
         
   /* Initialise the screen  */    
   mywin = initscr();
   noecho();
   raw();  
   keypad(stdscr, TRUE);       
   scrollok(mywin,1);    
   idcok(mywin, 1); 
   idlok(mywin, 1);   
   /*  Get the size of the window  */ 
   getmaxyx(mywin, nrows, ncols); 
   clear(); 
   refresh(); 
   
   /*  Set row and col */ 
   r=0; c=0; 
      
   /*  The main loop  */  
   while(1) 
   {  
          
     keyhandler(); 
                
   } 
                   
   echo(); 
   keypad(mywin, 0); 
   endwin();
   
   return 0; 
                  
}




