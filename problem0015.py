# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# example:problem0015.png
# How many such routes are there through a 20×20 grid?
import numpy as np

depth=20

mx=np.zeros((depth+1,depth+1))
print(mx)

for i in range(len(mx)):
    mx[i][-1:]=1
    if i==len(mx)-1:
        for j in range(len(mx[i])):
            mx[i][j]=1
print(mx)
for i in range(len(mx)-2,-1,-1):
    for j in range(len(mx)-2,-1,-1):
        a=mx[i][j+1]
        b=mx[i+1][j]
        print(a)
        print(b)
        mx[i][j]=a+b
print(mx)