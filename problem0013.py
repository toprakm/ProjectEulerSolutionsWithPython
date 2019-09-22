#   Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
#   Numbers are in problem0013_nums.txt

with open("problem0013_nums.txt") as file:
    for i in file:
        print (i.strip())