

# macrolang.py 
# A program to introduce the macro language used in pdeditor. 

# "TECO" was a popular macro language of the past. It was 
# extremely terse but packed an enormous amount of power in its 
# concise statements. 

# This macro language is inspired by TECO. Although this language is 
# nowhere near as concise or powerful, it may be of some use in 
# automating tasks in pdeditor. 

# *** Syntax *** 
# The main statements are as follows - 
# Moving the cursor - 7l, 7r, 7u, 7d - move 7 places to the left, right,
# up or down.   
# Move to a given place - (5, 27)m - Move to line 5, col 27.  

# Save a file - "mystuff.txt"w - (for "write") 
# Open a file - "mystuff.txt"o - (for "open") 
# Search for text -  /foo/s (for "search") 
# Replace text -  /foo/bar/r  (for "replace") 
# Print some text -  "This is a test"p (for "print") 

# Copy text -  "some stuff"c 
# ( Note - you then use a "move" command to move to the place that you 
# want to paste the text.  
# Paste text -  "some stuff"p ( Paste text at the position you moved to. 
# Paste text (method 2) - "some stuff"(7, 42)p 

# Move text - "some stuff"m(3, 25)(6, 42) - Moves text from line 3 col 25 
# to line 6 col 42.  
# Delete text - "some stuff"d 
# Delete all occurrences of a string - "some stuff"da 












 

 
