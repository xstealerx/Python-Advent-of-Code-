import string
lines = []
with open("2022/Day3_input.txt") as f:
    lines =  f.readlines()


left = []
right = []
for ele in lines:
    lenght = 0
    ele = ele.replace("\n", "")
    length = len(ele)
    splitter = int(length   /2 )
    left.append(ele[0:splitter])
    right.append(ele[splitter:length])

count = -1 
solution = []
for ele in left:
    count += 1
    max = len(ele)
    for i in range(max):
        char = ele[i]
        if (right[count].find(char) != -1):
            solution.append(char)
            break
print(solution)
sum = 0
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' , 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for ele in solution:
    for i in range (52):
        if(letters[i].find(ele) != -1) :
            sum += i +1 

print(sum)


     