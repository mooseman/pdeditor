

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
      # Replace spaces with "\s"  
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
      
      
# A function to track the repeated occurrences of some characters. 
# It notes their first and last positions.         
def track(mylist):       
    poslist = [] 
    charlist = [] 
    
    # A list to hold only the special chars that we are interested in 
    specialcharlist = [] 
    # A list to hold their position in the original list.
    specialcharposlist = [] 
    
    alldata = {} 
    repeatdict = {"^D": [], "^E": [], "^C": [], "^B": [], "^J": [], "\s": []} 
    # The characters to look for repeats of. 
    chardict = {"^D": 0, "^E": 0, "^C": 0, "^B": 0, "^J": 0, "\s": 0} 
    # We want to store the position in the list that a charcter occurs. 
    # We also want to store the range of positions that repeated 
    # characters cover. 
    
    # Replace spaces with "\s" 
    for char in mylist: 
       if char == " ": 
          char = "\s" 
       else: 
          char = char      
         
    poslist.append(mylist.index(char)) 
    charlist.append(char) 
      
    if chardict.has_key(char): 
       specialcharlist.append(char) 
       specialcharposlist.append(mylist.index(char)) 
            
            
                  
    # Update the dict which contains all of the data.   
    for k, v in zip(poslist, charlist): 
       alldata.update({k: v}) 
                               
    # Update the repeatdict dictionary               
    for k, v in zip(poslist, charlist): 
       alldata.update({k: v})                        
       myindex = mylist.index(char) 
       mylist = repeatdict[char] 
       mylist.append(myindex)                 
       repeatdict.update({char: mylist })       
    else: 
       pass    
         
    # Print the repeat dictionary 
    for k, v in repeatdict.items(): 
       print k, v 
       
                        
# Test the functions 
translate(charlist) 

track(charlist) 


 
         
                             
   








 






  

  
