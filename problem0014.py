# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

import numpy as np

kontrol=np.zeros(1000000, dtype=int)
print(type(kontrol))
kontrol[1]=1


def calc(num):
    chain=[]
    chain.append(num)
    numyedek=num
    sayac = 0
    while (num != 1):
        sayac = sayac + 1
        if num % 2 == 0:
            num = int(num / 2)
            if num < 1000000:
                if kontrol[num] != 0:
                    sayac=sayac+kontrol[num]
                    num=1
        else:
            num = int((3 * num) + 1)
            if num<1000000:
                if kontrol[num]!=0:
                    sayac=kontrol[num]
                    num=1
        chain.append(num)
    temp=0
    for i in chain:
        if i<1000000:
            kontrol[i]=sayac-temp
        temp=temp+1

    return sayac

for i in range (2,1000000):
    calc(i)


counter=0
enb=0
enbIndex=0
for i in kontrol:
    if enb<i:
        enb=i
        enbIndex=counter
    counter=counter+1
print(enb)
print(enbIndex)