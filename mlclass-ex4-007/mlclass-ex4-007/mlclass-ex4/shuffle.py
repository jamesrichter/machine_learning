import random
elements = []
with open('rawdata.csv','r+') as fileObj:
   for line in fileObj:
      elements.append(line)
      
random.shuffle(elements)

with open('rawrandomdata.csv','w+') as fileObj2:
   for element in elements:
      fileObj2.write(element)
      fileObj2.write(';')