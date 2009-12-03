

#  curses_crosstab.py 
#  Creating a crosstab in curses using Python 

#  Open a file and read in some data

import fileinput, csv, string 


class crosstab(object): 
   # Labels for variables - these are the columns headings 
   def init(self): 
      self.mylabels = [] 
      self.mylist = [] 
      self.mydict = {} 
      
   def read(self, file): 
      
   
   
   

def foo(it):
   mydict.update({tuple(it[0:2]):  it[2]}) 
   
#csv_data = list(csv.reader("testdata.csv")) 

a = ("North", "Red", 123)
b = ("West", "Blue", 456)
c = ["East", "Brown", 789]

mydict.update({tuple(a[0:2]):  a[2]}) 
mydict.update({tuple(b[0:2]):  b[2]}) 
mydict.update({tuple(c[0:2]):  c[2]}) 
   
print mydict 

x = list(mydict.keys()) 
print x 
      
print len(x)    

for e in x: 
  print e[0] 
  
for e in x: 
  print e[1]  
  







