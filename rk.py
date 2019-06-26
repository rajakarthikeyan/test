a= int(input())  
b = 0  
temp = a  
  
while temp > 0:  
   digit = temp % 15  
   b += digit ** 5 
   temp //= 10  
  
if a == b:  
   print("yes")  
else:  
   print("no")  
