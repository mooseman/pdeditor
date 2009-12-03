

#  curses_crosstab.py 
#  Creating a crosstab in curses using Python 

#  Open a file and read in some data

import fileinput, csv, string 


class crosstab(object): 
   # Labels for variables - these are the columns headings 
   def init(self): 
      self.mylabels = [] 
      self.mylist = [] 
      self.testlist = []
      self.mydict = {} 
      
   def read(self, file): 
      csv_data = list(csv.reader(open(file, "r")))[1:] 
      dict_data = list(csv.DictReader(open(file, "r"))) 
      for line in csv_data: 
         for x in line: 
            if x.isdigit():                 
               line[line.index(x)] = int(x) 
            else: 
               pass    
         # Get rid of newlines     
         if line != []:                 
            self.mylist.append(line)
         else: 
            pass    
   
      for line in dict_data:  
         for x in line: 
            if x.isdigit():                 
               line[line.index(x)] = int(x) 
            else: 
               pass    
         # Get rid of newlines     
         if line != []:                 
            self.testlist.append(line)
         else: 
            pass 
      
      
   
   def display(self): 
      print self.mylist[0][0:3] 
      print self.mylist[1][0:3]  
      
   def display2(self): 
      print self.testlist 
            
      
    
# Run the code 
a = crosstab() 
a.init()
a.read('testdata.csv') 
#a.display()      
a.display2() 

      





