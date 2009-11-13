

#  pdeditor.py 
#  A small and simple text editor. 

#  This code is released to the public domain.  

import sys, curses, curses.ascii, traceback, string, os 
   
#  A class to handle keystrokes  
class keyhandler:
    def __init__(self, scr): 
       self.scr = scr                       
       # Dictionary to store our data in.   
       self.data = {}                      
       self.stuff = ""        
       # A variable to save the line-number of text. 
       self.win_y = self.win_x = 0  
       # The top line 
       self.topline = 0
       self.bottomline = 23 
              
       (self.max_y, self.max_x) = self.scr.getmaxyx()     
       curses.noecho() 
       self.scr.keypad(1)            
       self.scr.scrollok(1)
       self.scr.idlok(1)  
       self.scr.setscrreg(0, 23)                                
       self.scr.refresh()	    
                          
    def set_y(self, val): 
       (y, x) = self.scr.getyx() 
       self.win_y += val 
                     
    def displaydict(self): 
       (y, x) = self.scr.getyx()  
       self.scr.addstr(y, x, str(self.data.items()) )     
       self.scr.refresh() 
                                                       
    # A function which points to the "top line" - the one which is 
    # currently at the top of the screen. Each line that the screen 
    # scrolls up will increase this number by 1. Each line scrolled 
    # down will decrease it by 1.  
    def pointtotopline(self, num): 
       self.topline = self.topline + num   
       
    def pointtobottomline(self, num): 
       self.bottomline = self.bottomline + num        
       
           
    # Retrieve data that has scrolled off the top of the screen 
    def retrievetop(self): 
       (y, x) = self.scr.getyx()  
       self.myval = self.topline - 1 
       if self.data.has_key(self.myval):  
            self.scr.addstr(y, 0, str(self.data[self.myval] ) )                 
       else: 
            pass             
       self.scr.refresh() 
       
    # Retrieve data that has scrolled off the bottom of the screen 
    def retrievebot(self): 
       (y, x) = self.scr.getyx()  
       self.myval = self.bottomline + 1 
       if self.data.has_key(self.myval):  
            self.scr.addstr(y, 0, str(self.data[self.myval] ) )                             
       else: 
            pass             
       self.scr.refresh()     
       
              
    def display(self): 
       (y, x) = self.scr.getyx()  
       if self.data.has_key(self.win_y):              
            mystuff = self.stuff + "fooble" 
            self.scr.addstr(y, 0, self.stuff )                 
       else: 
            pass             
       self.scr.refresh()  
       
       
    # Save a line of text into the dictionary.    
    def saveline(self): 
       (y, x) = self.scr.getyx()  
       # Save the line of text
       #self.stuff = self.scr.instr(y,0, len(self.stuff) )  
       self.stuff = self.scr.instr(y,0, self.max_x )         
       # Remove whitespace from the end of the line 
       self.stuff = self.stuff.rstrip()         
       # Save data to the dict using our win_y as the key. This is 
       # incremented and decremented as required. We can't just use
       # "y" as it is restricted to between 0 and max_y.   
       self.data.update({self.win_y: self.stuff})   
       self.stuff = ""  
          
    # Get a previously-saved line of text and display it 
    def getline(self):        
       if self.data.has_key(self.win_y): 
          myline = self.stuff  
          self.scr.addstr(self.win_y, 0, str(myline) ) 
       else: 
          pass              
       self.scr.refresh() 
               
                                                                                        # Trim the line when the backspace key is used              
    def trimline(self): 
       (y, x) = self.scr.getyx() 
       if x >= 1: 
          self.scr.move(y, x-1)     
          self.scr.delch(y, x)   
       elif x == 0: 
          self.scr.delch(y, x)                        
       else: 
          pass           
                                                        
    # Remove a character from the line (usually in the middle) 
    def removechar(self): 
       (y, x) = self.scr.getyx()    
       self.scr.delch(y, x)   
                                     
                                         
    def action(self):  
       while (1): 
          curses.echo()                 
          (y, x) = self.scr.getyx()                   
          c=self.scr.getch()		# Get a keystroke               
          if c in (curses.KEY_ENTER, 10):  
             curses.noecho()                
             self.saveline()               
             if y < self.max_y-1:  
                self.scr.move(y+1, 0)                     
                self.set_y(1)  
             else:                                              
                self.scr.scroll(1) 
                self.scr.move(y, 0)   
                self.set_y(1)  
                self.retrievebot()                            
                self.pointtotopline(1) 
                self.pointtobottomline(1)                                                              
             self.scr.refresh()   
          elif c==curses.KEY_BACKSPACE:  
             curses.noecho() 
             if x > 0:                  
                self.trimline()              
             else: 
                self.scr.deleteln() 
                self.set_y(-1)              
             self.scr.refresh()   
          elif c==curses.KEY_DC:  
             curses.noecho()                
             self.removechar()                                               
             self.scr.refresh()                                         
          elif c==curses.KEY_UP:  
             curses.noecho()              
             if y > 0:                                   
                self.scr.move(y-1, x)                    
                self.set_y(-1)                                                    
             elif y <= 0:   
                self.scr.scroll(-1)   
                self.scr.move(y, x)  
                self.set_y(-1) 
                self.retrievetop()                               
                self.pointtotopline(-1)   
                self.pointtobottomline(-1)                               
             self.scr.refresh()
          elif c==curses.KEY_DOWN:
             curses.noecho()               
             if y < self.max_y - 1:                 
                self.scr.move(y+1, x)   
                self.set_y(1)                                                               
             else:                                          
                self.scr.scroll(1)                 
                self.scr.move(y, x)  
                self.set_y(1)   
                self.retrievebot()                                              
                self.pointtotopline(1) 
                self.pointtobottomline(1)                                                 
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
          # Page Up. 
          elif c==curses.KEY_PPAGE: 
             (y, x) = self.scr.getyx()   
             self.scr.addstr(y, x, "You pressed Page Up!" )               
             self.scr.refresh()  
          # Page Down. 
          elif c==curses.KEY_NPAGE: 
             (y, x) = self.scr.getyx()   
             self.scr.addstr(y, x, "You pressed Page Down!" )               
             self.scr.refresh()                                             
          # Function keys. Note that we have not included F1, F10 or 
          # F11 here as they are difficult to "intercept". They invoke 
          # already built-in functionality.  
          elif c==curses.KEY_F2: 
             (y, x) = self.scr.getyx()   
             self.scr.addstr(y, x, "You pressed F2!" )               
             self.scr.refresh()  
          elif c==curses.KEY_F3: 
             (y, x) = self.scr.getyx()   
             self.scr.addstr(y, x, "You pressed F3!" )               
             self.scr.refresh()  
          elif c==curses.KEY_F4: 
             (y, x) = self.scr.getyx()   
             self.scr.addstr(y, x, "You pressed F4!" )               
             self.scr.refresh()  
          elif c==curses.KEY_F5: 
             (y, x) = self.scr.getyx()   
             self.scr.addstr(y, x, "You pressed F5!" )               
             self.scr.refresh()  
          elif c==curses.KEY_F6: 
             (y, x) = self.scr.getyx()   
             self.scr.addstr(y, x, "You pressed F6!" )               
             self.scr.refresh()  
          elif c==curses.KEY_F7: 
             (y, x) = self.scr.getyx()   
             self.scr.addstr(y, x, "You pressed F7!" )  
             self.scr.refresh() 
          elif c==curses.KEY_F8: 
             (y, x) = self.scr.getyx()   
             self.scr.addstr(y, x, "You pressed F8!" )               
             self.scr.refresh()                                
          elif c==curses.KEY_F9: 
             (y, x) = self.scr.getyx()   
             self.scr.addstr(y, x, "You pressed F9!" )               
             self.scr.refresh()                                
          elif c==curses.KEY_F12: 
             (y, x) = self.scr.getyx()   
             self.scr.addstr(y, x, "You pressed F12!" )               
             self.scr.refresh()                                
                          
          # If the terminal window is resized, take some action 
          elif c==curses.KEY_RESIZE: 
             (y, x) = self.scr.getyx()  
             (self.max_y, self.max_x) = self.scr.getmaxyx()     
             self.scr.addstr(y, x, "You resized the terminal!" ) 
             self.scr.addstr(y+1, x, str("Max row is now " + str(self.max_y) ) ) 
             self.scr.refresh()     
                                                          
          # Ctrl-G quits the app                  
          elif c==curses.ascii.BEL: 
             break      
          # Ctrl-A prints the data in the dict 
          elif c==curses.ascii.SOH:              
             self.displaydict()                           
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

