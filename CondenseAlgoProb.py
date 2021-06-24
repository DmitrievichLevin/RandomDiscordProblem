fulldata = [i for i in range(54)]
CHUNK = 3
threeList = []
threeByThree = []
finalByThree = []




for x in range(0, len(fulldata), 3):
    
        threeList.append([fulldata[j+x]for j in range(3)]) # here
    
for z in range(0, len(threeList), 3):
    
    threeByThree.append([threeList[y+z]for y in range(3)])


for d in range(2):
    for i in range(3):
            finalByThree.append([threeByThree[r+(d*3)][i]for r in range(3)]) # here
            
            
for h in finalByThree:
    for f in range(3):
        print(h[f], sep = '/n') 
