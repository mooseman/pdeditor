

#  pdspread.py  
#  A simple Python spreadsheet using curses.  
#  Acknowledgement - This app was inspired by David Mertz's 
#  txt2HTML curses-based utility in his "Charming Python" column 
#  (installment 6). A lot of code from that application is used here. 

#  This code is released to the public domain. 


import curses, curses.ascii, traceback, string, os

#-- Define the appearance of some interface elements
hotkey_attr = curses.A_BOLD | curses.A_UNDERLINE
menu_attr = curses.A_NORMAL

#-- Define additional constants
EXIT = 0
CONTINUE = 1

#-- Give screen module scope
screen = None

# A function to map Ctrl+letter to its ASCII code. 
def mapkeys(key): 
   pass 



#-- Create the topbar menu
def topbar_menu(menus):
    left = 2
    for menu in menus:
        menu_name = menu[0] 
        if menu_name == "Format":    
           menu_hotkey = menu_name[1] 
           menu_no_hot = menu_name[2:]                    
           screen.addstr(1, left, "F", menu_attr) 
           screen.addstr(1, left+1, "o", hotkey_attr)
           screen.addstr(1, left+2, "rmat", menu_attr)                                                                                  
        else:
           menu_hotkey = menu_name[0]            
           menu_no_hot = menu_name[1:]                
           screen.addstr(1, left, menu_hotkey, hotkey_attr)
           screen.addstr(1, left+1, menu_no_hot, menu_attr)                                                      
        left = left + len(menu_name) + 3
        # Add key handlers for this hotkey
        # NOTE - TO DO - This is where we can change the key-handling 
        # to use Ctrl or Alt.  
        topbar_key_handler(( curses.ascii.ctrl(string.upper(menu_hotkey)), menu[1]))
        topbar_key_handler(( curses.ascii.ctrl(string.lower(menu_hotkey)), menu[1]))
    # Little aesthetic thing to display application title
    screen.addstr(1, left-1, 
                  "*"*(52-left)+ " PD Editor ****",
                  curses.A_STANDOUT) 
    screen.refresh()


#-- Magic key handler both loads and processes keys strokes
#  TO DO - Make the menus accessed using either Ctrl or Alt. 
#  This will "free up" the "normal" keys to be used in editing 
#  as normal.     
def topbar_key_handler(key_assign=None, key_dict={}):
    if key_assign:
        key_dict[ord(key_assign[0])] = key_assign[1]
    else:
        c = screen.getch()
        if c in (curses.KEY_END, curses.KEY_UP, curses.KEY_DOWN, 
            curses.KEY_LEFT, curses.KEY_RIGHT, ord('!')):
            return 0
        elif c not in key_dict.keys():              
            curses.beep()
            return 1
        else:
            return eval(key_dict[c])


def file_func():
    s = curses.newwin(8,10,2,1)
    s.box()
    s.addstr(1,2, "N", hotkey_attr)
    s.addstr(1,3, "ew", menu_attr)
    s.addstr(2,2, "O", hotkey_attr)
    s.addstr(2,3, "pen", menu_attr)
    s.addstr(3,2, "S", hotkey_attr)
    s.addstr(3,3, "ave", menu_attr)
    s.addstr(4,2, "Save ", menu_attr)
    s.addstr(4,7, "A", hotkey_attr)
    s.addstr(4,8, "s", menu_attr)
    s.addstr(5,2, "Q", hotkey_attr)
    s.addstr(5,3, "uit", menu_attr)
    s.addstr(1,2, "", hotkey_attr)
    s.refresh()
    c = s.getch()
    if c in (ord('N'), ord('n')):  # New file 
        curses.echo() 
        s.erase() 
        curses.noecho() 
    elif c in (ord('O'), ord('o')):  
        curses.echo() 
        s.erase()        
        curses.noecho()    
    elif c in (ord('S'), ord('s')):
        curses.echo()
        s.erase()        
        curses.noecho()    
    elif c in (ord('A'), ord('a')):
        curses.echo()        
        s.erase()
        curses.noecho() 
    elif c in (ord('Q'), ord('q')):         
        curses.endwin() 
    else:
        curses.beep()
        s.erase()        
    return CONTINUE


def edit_func():    
    s = curses.newwin(6,10,2,8)
    s.box()
    s.addstr(1,2, "C", hotkey_attr)
    s.addstr(1,3, "opy", menu_attr)
    s.addstr(2,2, "P", hotkey_attr)
    s.addstr(2,3, "aste", menu_attr)
    s.refresh()
    c = s.getch()
    if c in (ord('C'), ord('c')):  
        curses.echo() 
        s.erase() 
        curses.noecho() 
    elif c in (ord('P'), ord('p')):  
        curses.echo() 
        s.erase()        
        curses.noecho()    
    else:
        curses.beep()
        s.erase()   
    return CONTINUE


def insert_func(): 
    s = curses.newwin(6, 15, 2, 15)
    s.box()
    s.addstr(1, 2, "C", hotkey_attr)
    s.addstr(1, 3, "olumn", menu_attr)
    s.addstr(2, 2, "R", hotkey_attr)
    s.addstr(2, 3, "ow", menu_attr)
    s.addstr(3, 2, "F", hotkey_attr)
    s.addstr(3, 3, "unction", menu_attr)
    s.addstr(4, 2, "H", hotkey_attr)
    s.addstr(4, 3, "yperlink", menu_attr)
    s.addstr(4, 2, "", hotkey_attr)
    s.refresh()
    c = s.getch()
    s.erase()
    
    if c in (ord('C'), ord('c')):  
       curses.echo()        
       s.erase()
       curses.noecho()          
    elif c in (ord('R'), ord('r')): 
       curses.echo()        
       s.erase()
       curses.noecho()     
    elif c in (ord('F'), ord('f')):        
       curses.echo()        
       s.erase()
       curses.noecho()          
    elif c in (ord('H'), ord('h')): 
       curses.echo()        
       s.erase()
       curses.noecho()                      
    else: curses.beep()
    return CONTINUE


def format_func():    
    s = curses.newwin(6,10,2,24)
    s.box()
    s.addstr(1,2, "C", hotkey_attr)
    s.addstr(1,3, "ell", menu_attr)
    s.addstr(2,2, "C", menu_attr)  
    s.addstr(2,3, "o", hotkey_attr) 
    s.addstr(2,4, "lumn", menu_attr) 
    s.addstr(3,2, "R", hotkey_attr)
    s.addstr(3,3, "ow", menu_attr)
    s.refresh()
    c = s.getch()
    if c in (ord('C'), ord('c')):  
        curses.echo() 
        s.erase() 
        curses.noecho() 
    elif c in (ord('O'), ord('o')):  
        curses.echo() 
        s.erase()        
        curses.noecho() 
    elif c in (ord('R'), ord('r')):  
        curses.echo() 
        s.erase()        
        curses.noecho()                 
    else:
        curses.beep()
        s.erase()   
    return CONTINUE


def data_func():    
    s = curses.newwin(6,10,2,33)
    s.box()
    s.addstr(1,2, "S", hotkey_attr)
    s.addstr(1,3, "ort", menu_attr)
    s.addstr(2,2, "F", hotkey_attr)
    s.addstr(2,3, "ilter", menu_attr)
    s.refresh()
    c = s.getch()
    if c in (ord('S'), ord('s')):  
        curses.echo() 
        s.erase() 
        curses.noecho() 
    elif c in (ord('F'), ord('f')):  
        curses.echo() 
        s.erase()        
        curses.noecho()    
    else:
        curses.beep()
        s.erase()   
    return CONTINUE


#-- Display the currently selected options
def draw_dict():
    '''screen.addstr(5,33, " "*43, curses.A_NORMAL)
    screen.addstr(8,33, " "*43, curses.A_NORMAL)
    screen.addstr(11,33, " "*43, curses.A_NORMAL)
    screen.addstr(14,33, " "*43, curses.A_NORMAL)
    screen.addstr(17,33, " "*43, curses.A_NORMAL)
    screen.addstr(5, 33, "This", curses.A_STANDOUT)
    screen.addstr(8, 33, "is", curses.A_STANDOUT)
    screen.addstr(11,33, "a", curses.A_STANDOUT)
    screen.addstr(14,33, "cuddly", curses.A_STANDOUT)
    screen.addstr(17,33, "moose", curses.A_STANDOUT) ''' 
    screen.refresh()


#-- Top level function call (everything except [curses] setup/cleanup)
def main(stdscr):
    # Frame the interface area at fixed VT100 size
    global screen
    screen = stdscr.subwin(23, 79, 0, 0)
    screen.box()
    screen.hline(2, 1, curses.ACS_HLINE, 77)
    screen.refresh()

    # Define the topbar menus
    file_menu = ("File", "file_func()")
    edit_menu = ("Edit", "edit_func()")
    insert_menu = ("Insert", "insert_func()")
    format_menu = ("Format", "format_func()")
    data_menu = ("Data", "data_func()")
    exit_menu = ("Quit", "EXIT")

    # Add the topbar menus to screen object
    topbar_menu((file_menu, edit_menu, insert_menu, format_menu, data_menu, exit_menu))

    # THIS LINE POSITIONS THE CURSOR     
    # (21, 76) is in the bottom-right corner of the window 
    # (3,2) is in the top-left corner of the window    
    ## screen.addstr(21, 76, "", curses.A_STANDOUT)  
    screen.addstr(3, 2, "", curses.A_STANDOUT)   
    draw_dict()
  
    # Enter the topbar menu loop
    while topbar_key_handler():
        draw_dict()


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

