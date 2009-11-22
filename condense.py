

# condense.py 

# A program to condense recorded macro data into a more compact form. 
# This "condensed" form can then be the basis of a macro language. 
# To start with, we want to condense things like consecutive whitespace
# and control characters (e.g. the arrow keys) 

charlist = ['^B', '^B', '^D', '^D', '^D', '^D', '^D', '^D', '^D', '^D', 
  '^D', '^D', '^F', '^B', ' ', 'T', 'h', 'i', 's', ' ', 'i', 's', ' ', 
  'a', ' ', 't', 'e', 's', 't', ' ', 'o', 'f', ' ', 'm', 'a', 'c', 'r', 
  'o', ' ', 'r', 'e', 'c', 'o', 'r', 'd', 'i', 'n', 'g', '.', ' ', 
  '^J', '^J', '^J', ' ', ' ', ' ', ' ', ' ', ' ',  
  '^E', '^E', '^E', '^E', '^E', '^E', '^E', '^E', '^E', '^E', '^B', 
  '^B', '^B', '^B', '^E', '^E', '^E', '^E', '^E', '^B', '^B', '^B', 
  '^D', '^D', '^D', '^D', '^D', '^D', '^D', '^D', '^D', '^D', '^D', 
  '^D', '^D', '^D', '^D', '^D', '^D', '^D', '^D', '^D', '^D', '^D', 
  '^B', '^B', '^B', '^B', '^B', '^E', '^E', '^E', '^E', '^E', '^E', 
  '^E', '^E', '^E', '^E', '^E', '^E', '^E', '^M']  
  
print len(charlist) 

# Now create a condensed version of the character list.  
# We will translate the space character to "\s". 
# Left-arrow is - ^D
# Right-arrow is - ^E 
# Up-arrow is - ^C
# Down-arrow is - ^B
# Enter is - ^J 


def translate(mylist): 
   # Create the dictionary 
   mydict = {} 
   newlist = [] 
   count = 0 
   
   # Each time one of our target characters (space, arrow keys, enter) 
   # appears, find out how many times it is repeated. Only then do we 
   # output the charcter (with its repetition count) to the new list. 
   mydict.update({"^D": 0, "^E": 0, "^C": 0, "^B": 0, "^J": 0, "\s": 0}) 
   
   # Now, first we just count how many times each of these characters 
   # appears in the input list. 
   for char in mylist: 
      if char == " ": 
         char = "\s" 
      else: 
         char = char           
              
      if mydict.has_key(char):          
         mydict.update({char: mydict[char]+1 }) 
      else: 
         pass 
         
   # Print the dict. 
   for k, v in mydict.items(): 
      print k, v 
      
   
# Test the function 
translate(charlist) 

 
         
                             
   








 






  

  
