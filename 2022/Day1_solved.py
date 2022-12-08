
import numpy as np 
lines = []
with open("2022/Day1_input.py") as f:
    lines= f.readlines()

arr = np.array
solution = 0
main = 0
solutionarr= []
for i in lines:
    ele = i.replace("\n","")
    if(ele != ""):
     solution += int(ele) 
    if(ele == ""):
        solutionarr.append(solution)
        solution = 0
arr = solutionarr
arr.sort()
length = len(arr)
print(arr[length-2])
print(arr[length-1])
print(arr[length-3])
print(arr[length-1] +arr[length-2] +arr[length-3])