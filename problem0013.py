#   Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
#   Numbers are in problem0013_nums.txt

top=0
add=0
with open("problem0013_nums.txt") as file:
    for i in file:
        add=int(i.strip())
        top=top+add
print(top)
s=str(top)
print("First 10 digits:",s[:10])