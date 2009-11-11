

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
              
       self.prevdata = {}        
       self.prevstuff = ""    
       self.stuff = "" 
       self.nextstuff = ''
       # A variable to save the line-number of text. 
       self.win_y = self.win_x = 0  
       # The top line 
       self.topline = 0
       self.bottomline = 23 
       
       (self.getbegy, self.getbegx) = self.scr.getbegyx()               
       (self.max_y, self.max_x) = self.scr.getmaxyx()     
       curses.noecho() 
       self.scr.keypad(1)            
       self.scr.scrollok(1)
       self.scr.idlok(1)  
       self.scr.setscrreg(0, 23)                                
       self.scr.refresh()	    
       
    # Override the builtin getyx() function. We will create a function
    # here which uses FIXED references - in other words, the origin 
    # does not move (as it does for the built-in func when scrolling is 
    # used). 
    # NOTE - when you scroll down past the bottom of the screen, the 
    # original "origin" scrolls off the top of the screen. So, we need     
    # to do a function which sets the "screen" origin to (say) 3, 0 
    # (if you have scrolled 3 lines past the bottom of the screen). 
                 
    def getyx(self): 
       #return (self.win_y, self.win_x)    
       return str(self.win_y) + "," + str(self.win_x)  
    
    # Change the value of self.win_y 
    # ( we don't really need a corresponding function for win_x ).
    # Here, we can compare win_y to the "built-in" y, and set win_y 
    # to zero if we want to.  
    
    # Override the built-in wmove (which can be a PITA... ) 
    def wmove(self): 
       pass 
    
    def set_y(self, val): 
       (y, x) = self.scr.getyx() 
       self.win_y += val 
                     
    # TO BE COMLETED 
    # compare self.win_y and y from self.scr.getyx() 
    def displaydict(self): 
       (y, x) = self.scr.getyx()  
       self.scr.addstr(y, x, str(self.data.items()) )     
       self.scr.refresh() 
                       
                                
    # Display the data in the dictionary 
    # This happens to be self.stuff.  
    # NOTE - add test to print hidden data (which has gone off the 
    # screen). Do this test when you press the up-arrow.  
    # Something like this - 
    # if self.data.has_key(self.win_y-1): 
    #    self.scr.addstr(y, 0, self.data[win_y-1])   
    
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
            #self.scr.addstr(y, 0, self.stuff )                 
       else: 
            pass             
       self.scr.refresh() 
       
       
    # Retrieve data that has scrolled off the bottom of the screen 
    def retrievebot(self): 
       (y, x) = self.scr.getyx()  
       self.myval = self.bottomline + 1 
       if self.data.has_key(self.myval):  
            self.scr.addstr(y, 0, str(self.data[self.myval] ) )                 
            #self.scr.addstr(y, 0, self.stuff )                 
       else: 
            pass             
       self.scr.refresh()     
       
       
    def display(self): 
       (y, x) = self.scr.getyx()  
       if self.data.has_key(self.win_y):  
            #self.scr.addstr(y, 0, str(self.data.values()) )     
            mystuff = self.stuff + "fooble" 
            self.scr.addstr(y, 0, self.stuff )                 
       else: 
            pass             
       self.scr.refresh()  
       
       
    # Save a line of text into the dictionary.    
    def saveline(self): 
       (y, x) = self.scr.getyx()  
       # Save the line of text
       self.stuff = self.scr.instr(y,0,len(self.stuff) )  
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
       self.scr.move(y, x-1)     
       self.scr.delch(y, x)   
                            
    # Remove a character from the line (usually in the middle) 
    def removechar(self): 
       (y, x) = self.scr.getyx()    
       self.scr.delch(y, x)   
                                     
                                         
    def action(self):  
       while (1): 
          curses.echo()                 
          #self.scr.scrollok(1) 
          #self.scr.idlok(1) 
          
          # Get the position of the cursor 
          (y, x) = self.scr.getyx()            
       
          c=self.scr.getch()		# Get a keystroke               
          if c in (curses.KEY_ENTER, 10):  
             curses.noecho()                
             self.saveline()               
             if y < self.max_y-1:  
                self.scr.move(y+1, 0)     
                self.set_y(1)   
                self.display()                                                
             else:                                              
                self.scr.scroll(1) 
                self.pointtotopline(1) 
                self.pointtobottomline(1)                 
                (y, x) = self.scr.getyx() 
                self.scr.move(y, 0) 
                #self.scr.mvwin(self.getbegy+1, 0)
                self.set_y(1)                 
                self.getbegy+1 
                self.display()                                                
                #self.scr.move(y, 0)  
             self.scr.refresh()   
          elif c==curses.KEY_BACKSPACE:  
             curses.noecho() 
             if x > 0:                  
                self.trimline()              
             else: 
                self.scr.deleteln() 
                self.set_y(-1) 
                self.display()                                                                                
             self.scr.refresh()   
          elif c==curses.KEY_DC:  
             curses.noecho()                
             self.removechar()                                               
             self.scr.refresh()                                         
          elif c==curses.KEY_UP:  
             curses.noecho() 
             #self.saveline()                                           
             if y > 0:                                   
                self.scr.move(y-1, x)                    
                self.set_y(-1)    
                self.display()                                                             
             elif y <= 0:   
                self.scr.scroll(-1)   
                self.scr.move(y, 0)  
                self.retrievetop()                               
                self.pointtotopline(-1)   
                self.pointtobottomline(-1)               
                self.display()                                                                                            
             self.scr.refresh()
          elif c==curses.KEY_DOWN:
             curses.noecho()  
             #self.saveline()                                                                   
             if y < self.max_y - 1:                 
                self.scr.move(y+1, x) 
                self.display()                                                
                self.set_y(1)                 
             else:                                          
                self.scr.scroll(1) 
                self.retrievebot() 
                self.pointtotopline(1) 
                self.pointtobottomline(1) 
                (y, x) = self.scr.getyx() 
                self.scr.move(y, x) 
                self.display()                                                
                self.set_y(1)                 
                self.getbegy+1 
                #self.getline()    
                #(y, x) = self.scr.getyx()              
                #self.scr.move(self.win_y, x)  
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
             self.displaydict() 
                          
          # Ctrl-R prints the screen data    
          elif c==curses.ascii.DLE: 
             self.displayscrdata()               
                          
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


   
