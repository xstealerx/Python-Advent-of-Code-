


lines = []
with open("2022/Day2_input.txt") as f:
    lines = f.readlines()
## X und A = Stein Y und B = Papier Z und C = Schere
solution = 0 
scoreX = 0
scoreY = 3
scoreZ = 6
for ele in lines:
    ele = ele.replace("\n", "")
    if ele[0] == "A":
        if ele[2] == "X":
            solution += 1
            solution += 3
        if ele[2] == "Y":
            solution += 2
            solution += 6
        if ele[2] == "Z":
            solution += 3
            solution += 0
    if ele[0] == "B":
        if ele[2] == "X":
            solution += 1
            solution += 0
        if ele[2] == "Y":
            solution += 2
            solution += 3
        if ele[2] == "Z":
            solution += 3
            solution += 6
    if ele[0] == "C":
        if ele[2] == "X":
            solution += 1
            solution += 6
        if ele[2] == "Y":
            solution += 2
            solution += 0
        if ele[2] == "Z":
            solution += 3
            solution += 3

print( solution)
solution = 0
## Part Two
for ele in lines:
    ele = ele.replace("\n", "")
    if ele[0] == "A":
        if ele[2] == "X":
            solution += 3
            solution += scoreX
        if ele[2] == "Y":
            solution += 1
            solution += scoreY
        if ele[2] == "Z":
            solution += 2
            solution += scoreZ
    if ele[0] == "B":
        if ele[2] == "X":
            solution += 1
            solution += scoreX
        if ele[2] == "Y":
            solution += 2
            solution += scoreY
        if ele[2] == "Z":
            solution += 3
            solution += scoreZ
    if ele[0] == "C":
        if ele[2] == "X":
            solution += 2
            solution += scoreX
        if ele[2] == "Y":
            solution += 3
            solution += scoreY
        if ele[2] == "Z":
            solution += 1
            solution += scoreZ

print( solution)