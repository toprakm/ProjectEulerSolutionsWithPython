# -*- coding: utf-8 -*-

# =============================================================================
# Problem 4 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.
# =============================================================================
result=0
for i in range(100,1000):
   for j in range(100,1000):
      mul=i*j
      x=str(mul)
      l=list(x)
#      print(l)
      lenght=len(l)
#      print(lenght)
      lenght2=lenght-1
      cor=1
      n=int((lenght/2))
#      print(n)
      for a in range(0,n):
         if l[a]!=l[lenght2-a]:
            cor=0
      if cor==1:
         if result<mul:
            result=mul
print(result)         
      