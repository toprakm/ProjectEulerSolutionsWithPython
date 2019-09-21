# =============================================================================
# 
# Problem 9 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# =============================================================================

for c in range (333,999):
   for b in range (2,499):
      for a in range (1,333):
         if a+b+c==1000 and b>a and c>b:
            if (a**2)+(b**2)==c**2:
               print(a,b,c,a*b*c)