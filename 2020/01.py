
# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))



numbers = []
with open("01.txt") as f:
    numbers = list(map(int, f.readlines()))
print(numbers)

for x in numbers:
    for y in numbers:
        if x+y == 2020:
            print(x)
            print(y)
            print(x*y)

for x in numbers:
    for y in numbers:
        for z in numbers:
            if x+y+z == 2020:
                print(x*y*z)

