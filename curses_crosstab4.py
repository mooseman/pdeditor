

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
      self.mydata = list(csv.reader(open(file, "r"))) 
      
      for line in self.mydata: 
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
                             
      self.test = zip(*self.mylist)   
           
      '''k = self.test[0][0]
      v = self.test[0][1:]
      self.mydict.update({k: v}) 
      k = self.test[1][0]
      v = self.test[1][1:]
      self.mydict.update({k: v}) 
      k = self.test[2][0]
      v = self.test[2][1:]
      self.mydict.update({k: v})  '''    
      
   def head(self, it): 
      it = list(it)
      print it[0] 
      
   def tail(self, it): 
      it = list(it)
      print it[1:]          
                   
      
      '''for i in range(0, 3): 
         for k, v in self.head(self.test[i]), self.tail(self.test[i]): 
             self.mydict.update({k: v}) '''                   
                   
                                                                                                                                    
   def display(self): 
      #print self.mylist
      print self.mylist[0][0:3] 
      print self.mylist[1][0:3]  
      print self.mylist[2][0:3]  
      print self.mylist[3][0:3]  
      
      
      
   def display2(self): 
      try: 
         while 1: print self.dict_data.next() 
      except StopIteration:
         pass 
          
   def display3(self): 
      print self.mydict 
      
   def display4(self): 
      print self.test[0][0]
      print self.test[0][1:]
      print self.test[1][0]
      print self.test[1][1:]
      print self.test[2][0]
      print self.test[2][1:]

      
# Run the code 
a = crosstab() 
a.init()
a.read('testdata.csv') 
a.head(["foo", "bar", "baz"]) 
a.tail(["foo", "bar", "baz"]) 
a.display3()      


      





