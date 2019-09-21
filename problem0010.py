# =============================================================================
# Problem 10 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.
# =============================================================================
theList=[]
for i in range(0,2000000):
   theList.append(i)
#   2.000.000 elemanlı liste, sıralı sayılar.

for i in range(2,1420):
   flag=True
   for j in range(2,int(i/2)+1):
      if i%j==0:
         flag=False
   
   if flag==False:
      mul=i
      add=i
      while mul<=1999999:
         theList[mul]=0
         mul=mul+add
      
   else:
      mul=i
      mul=mul+mul
      add=i
      while mul<=1999999:
         theList[mul]=0
         mul=mul+add
      

summ=-1
for i in theList:
   if i!=0:
      summ=summ+i               
print(summ)      