# -*- coding: utf-8 -*-

# =============================================================================
# Problem 3 
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?
# =============================================================================
num=600851475143
div=2
ldiv=0
while div<=num:
   if num%div==0:
      num=num/div
      ldiv=div
   else:
      div=div+1
print(ldiv)      