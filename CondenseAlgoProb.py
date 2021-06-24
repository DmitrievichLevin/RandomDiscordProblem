fulldata = [i for i in range(54)]
threeList = []
threeByThree = []




for x in range(0, len(fulldata), 3):
    
        threeList.append(fulldata[x:x+3]) 

for z in range(0, len(threeList), 9):
    for x in range(3):
    
        threeByThree.append(threeList[x+z:z+9:3])


            
            
for h in threeByThree:
    for f in range(3):
        print(h[f], sep = '/n') 
