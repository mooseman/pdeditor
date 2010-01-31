

#  head_tail.py 


class test(object): 

   def head(self, it):       
      return [list[0] for list in it] 
      
   def tail(self, it):       
      return [list[1:] for list in it]          
                   

a = test() 
l = ["foo", "bar", "baz"]
print a.head(l)
print a.tail(l) 


b = test() 
l = [ ["foo", "bar", "baz"], [1, 2, 3], ["just", "a", "test"] ]
print b.head(l)
print b.tail(l) 


 
l = [ ["foo", "bar", "baz"], [1, 2, 3], ["just", "a", "test"] ]

b = [list[0] for list in l]

c = [list[1:] for list in l]      
      
print b, c 

      


