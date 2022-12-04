


lines = []
with open("2022/Day4_input.txt") as f:
    lines = f.readlines()
solution = 0 
part2 = 0 
for ele in lines:
    ele = ele.replace("\n", "")
    first = ele.split(",")
    one = first[0]
    two = first[1]
    first_Values = one.split("-")
    second_Values = two.split("-")
    valueOne =int(first_Values[1])
    valueTwo =int(second_Values[1])
    if(valueOne > valueTwo):

        if(int(first_Values[0]) <= int(second_Values[0])):
             solution += 1
    if (valueOne < valueTwo):
        if(int(first_Values[0]) >= int(second_Values[0])):
      
                solution += 1 
    if (valueOne == valueTwo):
        solution += 1
    if (int(first_Values[1]) < int(second_Values[0])):
        part2 += 1
        print(ele)
    if (int(first_Values[0]) > int(second_Values[1])):
        part2 += 1
        print(ele)

part2 = len(lines)-part2
print(solution, part2)