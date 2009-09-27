

#  pdspread.py  
#  A simple Python spreadsheet using curses.   
#  This code is released to the public domain. 

#  Note - The Control keys are as follows - 
#  'SOH', 'STX', 'ETX', 'EOT', 'ENQ', 'ACK', 'BEL', 'BS', 
#  'HT', 'LF', 'VT', 'FF', 'CR', 'SO', 'SI', 'DLE', 'DC1', 
#  'DC2', 'DC3', 'DC4', 'NAK', 'SYN', 'ETB', 'CAN', 'EM', 'SUB' 
#  
#   We use the following here -  
#  ^Q (Quit),  ^H (Backspace),  ^S(Save), ^A(save As),  
#  ^B (Left-arrow) ^F(Right-arrow), ^P(Up-arrow), ^N(Down-arrow)      
import sys, curses, curses.ascii, curses.textpad, traceback, string, os

     
class cell(object): 
  def __init__(self): 
    self.width = 7 
    self.height = 2    
    self.text = "       " 
   
  def set(self, text): 
    self.text = text 
    
  def display(self):     
    return self.text      
               
               
class sheet(cell): 
  def init(self): 
    self.col = self.row = 0 
    # Draw the column and row headings 
    x = range(1, 11)
    y = range(1, 11)
    
    for val in x: 
      for val in y: 
        self.display() 
            
  def address(self): 
    return (self.col, self.row) 
    
  def move(self, col, row): 
    self.col = col 
    self.row = row 
            
  def write(self, col, row, text): 
    self.move(col, row)     
    cell.set(self, text)                       
               

#-- Define additional constants
EXIT = 0
CONTINUE = 1

#-- Give screen module scope
screen = None


# Key handler both loads and processes keys strokes
def topbar_key_handler(key_assign=None, key_dict={}):
    if key_assign:
        key_dict[ord(key_assign[0])] = key_assign[1]
    else:
        c = screen.getch()
        if c in (curses.KEY_END, ord('!')):
            return 0
        elif c not in key_dict.keys():
            curses.beep()
            return 1
        else:
            return eval(key_dict[c])



#-- Draw a cell on the screen 
#  NOTE - Cell contents are drawn relative to the CURRENT cell (window) 
#  - NOT the screen as a whole.  
def draw():  
  # Start at top-left of screen   
  x = y = 0   
  # Draw a cell 3 rows high and 12 columns wide, starting at y, x.  
  # Note - One row is needed for each of the borders, so this cell 
  # is really only one row high and ten columns wide.  
  mywin = curses.newwin(23, 80, y, x) 
  mywin.box()  
  mywin.addstr(0, 25, "*** P.D. Editor ***")   
  mywin.refresh() 
  mywin2 = mywin.subwin(21, 77, y+1, x+1)  
  mywin2.setscrreg(1, 20)
  mywin2.refresh() 
  myeditor = curses.textpad.Textbox(mywin2) 
  myeditor.edit() 
  # Get the position of the cursor and see if we need to scroll the 
  # text. 
  pos = mywin2.getyx() 
  if pos[0] >= 20: 
       mywin2.idlok(1) 
       mywin2.scrollok(1) 
       mywin2.scroll(1) 
  else: 
       pass         
    
  
#-- Top level function call (everything except [curses] setup/cleanup)
def main(stdscr):
    # Frame the interface area at fixed VT100 size
    global screen
    screen = stdscr.subwin(23, 79, 0, 0)
    # screen.box()
    # screen.hline(2, 1, curses.ACS_HLINE, 77)
    # screen.clear() 
    screen.refresh()
  
    # Enter the topbar menu loop
    while topbar_key_handler():
        draw()


#  Run this when the module is called from the command-line 
if __name__=='__main__':
    try:
        # Initialize curses
        stdscr=curses.initscr()
        #curses.start_color()
        # Turn off echoing of keys, and enter cbreak mode,
        # where no buffering is performed on keyboard input
        curses.noecho() ; curses.cbreak()

        # In keypad mode, escape sequences for special keys
        # (like the cursor keys) will be interpreted and
        # a special value like curses.KEY_LEFT will be returned
        stdscr.keypad(1)
        main(stdscr)                    # Enter the main loop
        # Set everything back to normal
        stdscr.keypad(0)
        curses.echo() ; curses.nocbreak()
        curses.endwin()                 # Terminate curses
    except:
        # In the event of an error, restore the terminal
        # to a sane state.
        stdscr.keypad(0)
        curses.echo() ; curses.nocbreak()
        curses.endwin()
        traceback.print_exc()           # Print the exception



