# =============================================================================
# Problem 5 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 
# =============================================================================
num=2520
b=1
dngu=0
dngu2=0
while b==1:
   dngu+=1
   if dngu==1000000:
      dngu2+=1
      print(dngu2)
      dngu=0
   num=num+20
   b=0
   i=3
   while i<21:
      if num%i!=0:
         b=1
         i=22
      i=i+1 
print(num)        
         