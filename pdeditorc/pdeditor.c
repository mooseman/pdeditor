

/*  pdeditor.c                                    */  
/*  A simple text-editor in C                     */ 
/*  Remember to compile this code with the        */ 
/*  -lncurses option. This links it with curses.  */  
/*  This code is released to the public domain.   */ 
/*  "Share and enjoy..."  ;)                      */ 


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <curses.h>


/* Declare our window  */ 
   WINDOW *mywin;  

/* The row and column of the cursor, and the number of */ 
/* rows and cols in the window. */  
int r, c, nrows, ncols;  

/* An array to hold the contents of a line */ 
/* Note - need to make sure that if you insert text which makes the line */
/* longer than 80 chars, then a new line array is created and text added */ 
/* to it. */ 
char text[80];  

/*  Character read from keyboard. */ 
/*  Note - make sure this is an INT variable. */ 
int ch; 

/*  Set insert mode to zero when we start. */ 
int insmode = 0; 

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
    
int insert() 
{    
   if (insmode == 0) insmode = 1; 
   else if (insmode == 1) insmode = 0;        
   return insmode; 
}     


void put(int ch)
{   
   getyx(mywin, r, c); 
   if (insmode == 0) addch(ch);    
   else if (insmode == 1) insch(ch); 
   refresh();     
}     


void test() 
{ 
   getyx(mywin, r, c); 
   addstr("Just a small test string..."); 
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
  else if (ch == KEY_IC)      insert();      
  else put(ch); 
                        
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




