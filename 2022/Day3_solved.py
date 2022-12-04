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
## part two 
part2 = []
for i in range(0,len(lines),3):
    
    for char in lines[i]:
        for i in range(len(char)):
            letter = char[i]
            if(lines[i+1].find(letter)!= -1):
                if(lines[i+2].find(letter)!= -1):
                  part2.append(letter)


part2_solution = 0    
for ele in part2:
    for i in range (52):
        if(letters[i].find(ele) != -1) :
            part2_solution += i +1
print("Lösung Zwei " + str(part2_solution))