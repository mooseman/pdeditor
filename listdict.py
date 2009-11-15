

# listdict.py
# A Dictionary which uses lists to store the keys and values

# >>> a = ["foo", "bar", "baz", "the", "quick"]
# >>> b = [1, 2, 3, 4, 5]
# >>> d = {}
# >>> for k, v in zip(b, a):
# ...    d.update({k: v})  
# ... 
# >>> d
# {1: 'foo', 2: 'bar', 3: 'baz', 4: 'the', 5: 'quick'}
# >>> 

# We can use the "del" function to remove list elements or slices - 
# >>> del b[2] 
# >>> b
# [1, 2, 4, 5]
# >>>  

a = [1, 2, 3, 4, 5]
b = ["foo", "bar", "baz", "the", "quick"]
d = {}

for k, v in zip(a, b):
    d.update({k: v})  
    
print d 

# Do the same thing using the enumerate() function 
for i, x in enumerate(b, 1):
    #print i, x
    d.update({i: x})  
    
print d  


for k, v in enumerate(d.values(), 1): 
    d.update({k: v})  
    
print d  

    






