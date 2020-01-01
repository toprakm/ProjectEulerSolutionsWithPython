# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?


a=2**1000
stra=str(a)
top=0
for i in stra:
    top=top+int(i)
print(top)    