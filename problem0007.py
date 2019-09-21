# =============================================================================
# Problem 7 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?
# =============================================================================
primeC=2
prime=0
i=3
while primeC<10001:
   i=i+2
   flag=1
   mx=int((i/2)+1)
   j=2
   while j<mx and flag==1:
      if i%j==0:
         flag=0
      if j==2:
         j+=1
      else:
         j+=2
   if flag==1:
      primeC+=1
      prime=i
      
print(prime)      
         