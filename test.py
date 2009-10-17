

#  editor.py 
#  A small and simple text editor. 

import sys, curses, curses.wrapper, curses.ascii, curses.textpad, \
   traceback, string, os 
   
# Note - look at customising the getmaxyx() method. Maybe do a 
# SETMAXYX method, where you can change the dimensions of the 
# EXISTING screen. The change could then be checked via getmaxyx.    
class keyhandler:
    def __init__(self, scr): 
       self.scr = scr   
       self.win_y, self.win_x = 0,0                
       (self.max_y, self.max_x) = self.scr.getmaxyx()     
       curses.echo()       
       self.scr.scrollok(1)
       self.scr.idlok(1)  
       self.scr.setscrreg(0, 23)                                
       self.scr.refresh()	    
       
    def getmaxyx(self): 
       return (self.max_y, self.max_x) 
       
    def setmax_y(self, val): 
       self.max_y = val 
       
    def setmax_x(self, val): 
       self.max_x = val        
       
    
    def action(self):  
       while (1): 
          curses.echo()                 
          self.scr.scrollok(1) 
          self.scr.idlok(1) 
          self.scr.setscrreg(0, 23)
          # Get the position of the cursor 
          (y, x) = self.scr.getyx()  
          self.win_y, self.win_x = y,x 
       
          c=self.scr.getch()		# Get a keystroke               
          if c in (curses.KEY_ENTER, 10):  
             curses.noecho()   
             (y, x) = self.scr.getyx() 
             if y < self.max_y-1:                 
                self.scr.move(y+1, 0)                    
             else:                            
                self.scr.scroll(1)    
                (y, x) = self.scr.getyx() 
                self.scr.move(y, 0)                             
             self.scr.refresh()   
          elif c==curses.KEY_BACKSPACE:  
             curses.noecho()           
             self.scr.move(y, x-1) 
             (y, x) = self.scr.getyx() 
             self.scr.delch(y, x)  
             self.scr.refresh()   
          elif c==curses.KEY_DC:  
             curses.noecho()           
             self.scr.delch(y, x) 
             self.scr.refresh()                                         
          elif c==curses.KEY_UP:  
             curses.noecho()           
             self.scr.move(y-1, x) 
             self.scr.refresh()
          elif c==curses.KEY_DOWN:
             curses.noecho()                           
             if y < self.max_y - 1:                 
                self.scr.move(y+1, x)                    
             else:                          
                self.scr.scroll(1)    
                self.scr.move(y, x)  
             self.scr.refresh()   
          elif c==curses.KEY_LEFT: 
             curses.noecho()           
             self.scr.move(y, x-1) 
             self.scr.refresh()
          elif c==curses.KEY_RIGHT: 
             curses.noecho() 
             self.scr.move(y, x+1) 
             self.scr.refresh() 
          elif c==curses.KEY_HOME: 
             curses.noecho() 
             self.scr.move(y, 0) 
             self.scr.refresh() 
          elif c==curses.KEY_END: 
             curses.noecho() 
             self.scr.move(y, 79) 
             self.scr.refresh() 
          # Ctrl-G quits the app                  
          elif c==curses.ascii.BEL: 
             break            
          elif 0<c<256:
             c=chr(c)              
             #curses.echo()            
             self.scr.refresh()  

#  Main loop       
def main(stdscr):  
    a = keyhandler(stdscr)      
    a.action() 
       
                                   
#  Run the code from the command-line 
if __name__ == '__main__':  
  try: 
     stdscr = curses.initscr()   
     curses.noecho() ; curses.cbreak()
     stdscr.keypad(1)
     main(stdscr)      # Enter the main loop
     # Set everything back to normal
     stdscr.keypad(0)
     curses.echo() ; curses.nocbreak()
     curses.endwin()  # Terminate curses
  except:
     # In the event of an error, restore the terminal
     # to a sane state.
     stdscr.keypad(0)
     curses.echo() ; curses.nocbreak()
     curses.endwin()
     traceback.print_exc()  # Print the exception


   
