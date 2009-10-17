

#  pdeditor.py 
#  A small and simple text editor. 

#  This code is released to the public domain.  


import sys, curses, curses.wrapper, curses.ascii, curses.textpad, \
   traceback, string, os 
   
# Note - Now that we have a dict for the data, we need to display the 
# data when the user scrolls back to a previously off-screen area. 
# First, we can test the display of the data using a Ctrl key to print
# it out.

# Useful stuff for backspace, delete keys 
# For delete key - need to get the "x" value of the deleted char, then 
# delete it from the linedata list.  
# >>> a = ["foobarbaz"]
# >>> c = a[0][0:len(a[0])-1] 
# >>> c 
# 'foobarba'  

 
class keyhandler:
    def __init__(self, scr): 
       self.scr = scr 
       # Dictionary to store our data in.   
       self.data = {} 
       self.linedata = []  
       self.stuff = "" 
       self.y, self.x = 0, 0                
       (self.max_y, self.max_x) = self.scr.getmaxyx()     
       curses.echo()       
       self.scr.scrollok(1)
       self.scr.idlok(1)  
       self.scr.setscrreg(0, 23)                                
       self.scr.refresh()	    
       
    # Display the data in the dictionary        
    def display(self): 
       (y, x) = self.scr.getyx()  
       self.scr.addstr(y, x, str(self.data.items()) )     
       self.scr.refresh()  
       
    # Save a line of text into the dictionary.    
    def saveline(self): 
       (y, x) = self.scr.getyx()  
       self.linedata.append(self.stuff) 
       self.data.update({y: self.linedata})   
       self.stuff = ""  
       self.linedata = [] 
        
    # Trim the line when the backspace key is used              
    def trimline(self): 
       (y, x) = self.scr.getyx() 
       self.stuff = self.stuff[0:len(self.stuff)-1]  
              
    # Remove a character from the line (usually in the middle) 
    def removechar(self): 
       (y, x) = self.scr.getyx() 
       self.stuff = self.stuff[0:x-1] + self.stuff[x+1:len(self.stuff)]
                   
                                         
    def action(self):  
       while (1): 
          curses.echo()                 
          self.scr.scrollok(1) 
          self.scr.idlok(1) 
          self.scr.setscrreg(0, 23)
          # Get the position of the cursor 
          (y, x) = self.scr.getyx()            
       
          c=self.scr.getch()		# Get a keystroke               
          if c in (curses.KEY_ENTER, 10):  
             curses.noecho()   
             self.saveline()              
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
             self.trimline()              
             self.scr.delch(y, x)               
             self.scr.refresh()   
          elif c==curses.KEY_DC:  
             curses.noecho()   
             (y, x) = self.scr.getyx() 
             self.removechar()                     
             self.scr.delch(y, x) 
             self.scr.refresh()                                         
          elif c==curses.KEY_UP:  
             curses.noecho()  
             self.saveline()              
             if y > 0:                   
                self.scr.move(y-1, x)                    
             else:                 
                self.scr.scroll(-1)         
                (y, x) = self.scr.getyx()   
                self.scr.move(self.win_y, x)                
             self.scr.refresh()
          elif c==curses.KEY_DOWN:
             curses.noecho() 
             self.saveline()                                                 
             if y < self.max_y - 1:                 
                self.scr.move(y+1, x)                    
             else:                                          
                self.scr.scroll(1)    
                (y, x) = self.scr.getyx() 
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
          # Ctrl-A prints the data in the dict 
          elif c==curses.ascii.SOH: 
             self.display() 
             
          elif 0<c<256:
             c=chr(c)   
             self.stuff += c                           
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


   
