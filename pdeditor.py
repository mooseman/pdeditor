

#  pdspread.py  
#  A simple Python spreadsheet using curses.  
#  Acknowledgement - This app was inspired by David Mertz's 
#  txt2HTML curses-based utility in his "Charming Python" column 
#  (installment 6). A lot of code from that application is used here. 

#  This code is released to the public domain. 


import sys, curses, curses.ascii, curses.textpad, traceback, string, os

myscreen = curses.initscr()
myscreen.border(0) 
myscreen.addstr(2, 2, "*** PD Editor ***")

myeditor = curses.textpad.Textbox(myscreen) 
myeditor.edit() 


myscreen.refresh()
myscreen.getch()

curses.endwin()





