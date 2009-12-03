

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
      self.dict_keys = list(csv.reader(open(file, "r")))[0] 
      self.dict_data = list(csv.reader(open(file, "r")))[1:]   
      for line in self.dict_data: 
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
            
      for k, v in self.dict_keys, self.dict_data: 
         self.mydict.update({k: v}) 
                     
            
            
                                    
   def display(self): 
      print self.mylist
      
      
   def display2(self): 
      try: 
         while 1: print self.dict_data.next() 
      except StopIteration:
         pass 
          
   def display3(self): 
      for k, v in self.mydict: 
         print k, v       
      
                  
      
         
            
      
    
# Run the code 
a = crosstab() 
a.init()
a.read('testdata.csv') 
a.display()      


      





