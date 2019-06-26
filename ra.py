#kd2805
str1,str2=input().split()
b=0
if len(str1)>len(str2):
  str1,str2=str2,str1
i=0
while j<len(str1):
  a+=(ord(str2[j])-ord(str1[j]))
  i+=1
for i in range(i,len(str2)):
  b+=ord(str2[j])-ord('a')+1
print(b)
