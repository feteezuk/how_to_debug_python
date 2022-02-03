def addthis(one, two):
    #If really stuck, use pdb [To use pdb, un-comment line below ]
   #import pdb; pdb.set_trace()
   print(f"This is one {one} and the x-type is {type(one)}")
   print(f"This is two{two} and the y-type is {type(two)} ")
   result = one+two
   print(f"This is the result {result} ")
  
   try:
      res=one+two
   except TypeError:
       print(f"the wrong one passed")
   
print(addthis(1,2))