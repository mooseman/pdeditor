

#  pdeditor.py 
#  A small and simple text editor. 

#  This code is released to the public domain.  

import sys, math, curses, curses.ascii, traceback, string, os 
   
#  A class to handle keystrokes  
class keyhandler:
    def __init__(self, scr): 
       self.scr = scr                       
       # Dictionary to store our data in.   
       self.data = {}           
       self.indexlist = [] 
       self.linelist = []            
       self.stuff = ""        
       # A variable to save the line-number of text. 
       self.win_y = self.win_x = 0  
       # The top line 
                   
       (self.max_y, self.max_x) = self.scr.getmaxyx()
       # Set page size (for page-up and page-down) 
       self.pagesize = self.max_y-1        
       curses.noecho() 
       self.scr.keypad(1)            
       self.scr.scrollok(1)
       self.scr.idlok(1)  
       self.scr.setscrreg(0, self.max_y-1)                                
       self.scr.refresh()	    
                          
    def set_y(self, val): 
       (y, x) = self.scr.getyx() 
       self.win_y += val 
    
    # Display some stuff 
    def display(self): 
       (y, x) = self.scr.getyx()  
       self.scr.addstr(y, x, str("self.win_y is " + str(self.win_y) 
         + " and y is " + str(y) ) ) 
       self.scr.refresh() 
    
    # Move to the next line 
    def nextline(self): 
       (y, x) = self.scr.getyx() 
       curses.noecho()                              
       self.saveline()               
       if y < self.max_y-1:  
          self.scr.move(y+1, 0)                     
          self.set_y(1)  
       else:                                              
          self.scr.scroll(1) 
          self.scr.move(y, 0)   
          self.set_y(1)  
          self.retrievedata(self.win_y, self.win_y)                 
       self.scr.refresh()   
        
    def pageup(self): 
       (y, x) = self.scr.getyx()  
       (self.max_y, self.max_x) = self.scr.getmaxyx()              
       if self.win_y > self.pagesize: 
          self.scr.move(self.win_y - self.pagesize, 0)                     
          self.set_y(self.win_y - self.pagesize)                 
       else: 
          self.scr.move(0, 0)                     
          self.set_y(-self.win_y) 
       self.scr.refresh() 
       
    # A version of pagedopwn which shows the lines that it is about 
    # to retrieve       
    def pagedowntemp(self):    
       (y, x) = self.scr.getyx()  
       (self.max_y, self.max_x) = self.scr.getmaxyx()  
       # The number of lines is the first line plus X more. 
       # So, this gets four lines 
       firstline = self.win_y + 10 
       lastline = firstline + 3 
       self.retrievedata(firstline, lastline)                 
       #self.scr.refresh() 
       
                      
    def pagedown(self): 
       (y, x) = self.scr.getyx()  
       (self.max_y, self.max_x) = self.scr.getmaxyx()  
       # Calculate the number of lines to scroll 
       # This will be the current line of the cursor plus the 
       # pagesize minus the diff between the current position and 
       # self.max_y. 
       
       # How many lines are we from the bottom of the screen? 
       linestobot = self.max_y - y 
       # The first line to get will be self.win_y + linestobot + 1 
       firstline = self.win_y + linestobot + 1 
       # How many lines after that do we need to get? 
       numlines = 10 
       # The last line to get
       lastline = firstline + numlines
       
       if self.win_y + 20 < self.max_y-1: 
           self.scr.move(self.win_y+20, x)  
           self.set_y(20) 
       else:                          
           self.scr.move(self.max_y-1, x)  
           self.scr.scroll(numlines)                 
           self.set_y(numlines)   
       # Note - need to change retrievedata to retrieve a range of lines
       # from the dict - not just one as at present. 
           self.retrievedata(firstline, lastline)                 
       self.scr.refresh() 
                                  
    # Print the values of y and self.win_y.      
    def print_ys(self): 
       (y, x) = self.scr.getyx()  
       self.scr.addstr(y, x, " y is " + str(y) + " and self.win_y is "  
          + str(self.win_y) )  
       self.scr.refresh()        
    
    # Display the stored data in the dict                  
    def displaydict(self): 
       (y, x) = self.scr.getyx()  
       # Calculate the number of lines that the printed text will need
       # We then increment the value of self.win_y by this number. 
       numlines = int(math.ceil(len(str(self.data.items())) / self.max_x))               
       self.scr.addstr(y, x, str(self.data.items()) )     
       if len(str(self.data.items())) >= self.max_x: 
          self.set_y(numlines) 
       else: 
          pass 
       self.scr.refresh() 
            
    # Display the data in the two lists used to create the dict. 
    # Not really needed now, but left here for debugging purposes.                 
    def displaylists(self):             
       (y, x) = self.scr.getyx()  
       # Calculate the number of lines that the printed text will need
       # We then increment the value of self.win_y by this number. 
       numlines1 = int(math.ceil(len(str(self.indexlist)) / self.max_x))         
       numlines2 = int(math.ceil(len(str(self.linelist)) / self.max_x))                
       self.scr.addstr(y, 0, str(self.indexlist) ) 
       if len(str(self.indexlist)) >= self.max_x: 
          self.set_y(numlines1) 
       else: 
          self.set_y(1) 
       self.scr.addstr(y+1, 0, str(self.linelist) ) 
       if len(str(self.linelist)) >= self.max_x: 
          self.set_y(numlines2) 
       else: 
          pass            
       #self.set_y(1)
       self.scr.refresh()   
                                                        
                  
    # Retrieve data that has scrolled off the screen
    # Note - need to change retrievedata to retrieve a range of lines
    # from the dict - not just one as at present.  
    # Find the number and range of lines that we need to retrieve 
    # (if any).     
    def retrievedata(self, startline, endline): 
       (y, x) = self.scr.getyx()         
       for my_y in range(startline, endline+1): 
          if self.data.has_key(my_y):  
               self.scr.addstr(y, 0, str(self.data[my_y] ) )   
               y = y + 1  
               self.scr.refresh()              
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
       # Has the line already been entered? 
       # If so, replace it. Otherwise, add it.  
       if self.win_y in self.indexlist: 
          self.linelist[self.win_y] = self.stuff 
       else: 
          self.indexlist.append(self.win_y) 
          self.linelist.append(self.stuff)         
       for k, v in zip(self.indexlist, self.linelist): 
         self.data.update({k: v}) 
       # Re-set self.stuff to missing          
       self.stuff = ""  
                    
    def insertline(self):  
       self.scr.insertln()  
       (y, x) = self.scr.getyx()               
       self.indexlist = []                                 
       self.linelist.insert(self.win_y, "")         
       for i, x in enumerate(self.linelist):
           self.indexlist.insert(i, i)  
       # Update the data dict 
       for k, v in zip(self.indexlist, self.linelist): 
           self.data.update({k: v})      
       self.scr.refresh() 
              
    def deleteline(self):        
       # If the line index is not in self.indexlist, just move to the 
       # left-most column and clear to the end of the line
       (y, x) = self.scr.getyx()        
       if self.win_y not in self.indexlist \
       or self.win_y > len(self.indexlist):            
          self.scr.move(y, 0) 
          self.scr.clrtoeol() 
          self.scr.refresh() 
       # If the line index IS in self.indexlist, delete the line.    
       else: 
          self.scr.deleteln()           
          (y, x) = self.scr.getyx()                
          self.indexlist = []                                 
          del self.linelist[self.win_y]  
          for i, x in enumerate(self.linelist):
              self.indexlist.insert(i, i)  
          # Update the data dict 
          for k, v in zip(self.indexlist, self.linelist): 
              self.data.update({k: v})            
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
             self.nextline()              
          elif c==curses.KEY_BACKSPACE:  
             curses.noecho() 
             if x > 0:                  
                self.trimline()              
             else:                 
                self.deleteline()
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
             elif y == 0 and self.win_y > 0:   
                self.scr.scroll(-1)   
                self.scr.move(y, x)  
                self.set_y(-1) 
                self.retrievedata(self.win_y, self.win_y)       
             else: 
                pass                                                                                     
             self.scr.refresh()
          elif c==curses.KEY_DOWN:
             curses.noecho()              
             if y < self.max_y-1:                 
                self.scr.move(y+1, x)   
                self.set_y(1)                                                               
             else:                                          
                self.scr.scroll(1)                 
                self.scr.move(y, x)  
                self.set_y(1) 
                self.retrievedata(self.win_y, self.win_y)                 
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
             self.pageup()              
          # Page Down. 
          elif c==curses.KEY_NPAGE: 
             self.pagedown() 
          # Function keys. Note that we have not included F1, F10 or 
          # F11 here as they are difficult to "intercept". They invoke 
          # already built-in functionality.  
          elif c==curses.KEY_F2: 
             self.insertline() 
             self.scr.refresh()  
          elif c==curses.KEY_F3: 
             self.deleteline()              
             self.scr.refresh()  
          elif c==curses.KEY_F4: 
             (y, x) = self.scr.getyx()   
             self.scr.addstr(y, x, "You pressed F4!" )               
             self.scr.refresh()  
          elif c==curses.KEY_F5: 
             self.display()                                       
          elif c==curses.KEY_F6: 
             self.displaylists() 
          elif c==curses.KEY_F7: 
             self.displaydict() 
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
             self.pagesize = self.max_y - 2               
             self.scr.refresh()     
                                                          
          # Ctrl-G quits the app                  
          elif c==curses.ascii.BEL: 
             break      
          # Ctrl-A prints the data in the dict 
          elif c==curses.ascii.SOH:    
             self.pagedowntemp() 
             #self.print_ys()                            
             #self.displaydict()    
             #self.displaylists()                        
          elif 0<c<256:               
             c=chr(c)   
             if x < self.max_x-2:  
                self.stuff += c                           
             else:                 
                self.nextline()                                    
             
                          
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

