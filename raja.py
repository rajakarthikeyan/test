aa=int(input())
bb=list(map(int,input().split()))
ee=0
for i in range(len(bb)-2):
    for x in range(i+1,len(bb)-1):
         for j in range(x+1,len(bb)):
            if bb[i]<bb[x]<bb[j] and i<x<j:
               ee+=1
print(ee)    
