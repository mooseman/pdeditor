

import string, itertools, curses, curses.ascii 


def test(input): 
   mydict = {"a": 0, "d": 0, "s": 0, "p":0, "o": 0} 
   result = ""
   typelist = [] 
   numlist  = [] 
   count = 0  
      
   for ch in input:             
      if ch.isalpha():       
         type = "a"                                    
      elif ch.isdigit(): 
         type = "d"                                     
      elif ch.isspace(): 
         type = "s"         
      elif curses.ascii.ispunct(ch):          
         type = "p"         
      else: 
         type = "o" 
      
      typelist.append(type) 
     
      mydict.update({type: mydict[type] + 1})  
   
   mylist = [[k, len(list(g))] for k, g in itertools.groupby(typelist)]
   for x in mylist: 
      result = result + str(x[1]) + str(x[0]) 
   
   print mylist 
   print result 
                               
   for k, v in mydict.items(): 
      print k, v 
   
   print typelist 
         
test("foo12345#$%^  435bar") 

         
                   
   
   
   

