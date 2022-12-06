


with open("2022/Day6_input.txt") as f:
    lines = f.readlines()


solution = 0
sollution_List = []
ele = lines[0]

for i in range(len(lines[0])):
   
    char = ele[0]
   
    ele = ele[1:]
    if i>=3:
        firstLetter =str( sollution_List[i-3])
        secondLetter = str(sollution_List[i-2])
        thirdLetter = str(sollution_List[i-1])
        fourthLetter = str(char)
        # if (char not in sollution_List):
        if (firstLetter != secondLetter and firstLetter != thirdLetter and firstLetter != fourthLetter and secondLetter != thirdLetter and secondLetter != fourthLetter and thirdLetter != fourthLetter):
             
                solution = i+1
                # break
    sollution_List.append(char)     
print("Die Lösung für Part 1 ist: " + str(solution)   )   
#Part 2
part2 = lines[0]
part2_solution= 0

for i in range(14,int(len(lines[0]))):
    checkarray = []
    
    char = sollution_List[i-1]
    for j in range(14):
        checkarray.append(sollution_List[j])
        
   

    if(char not in checkarray):

        converted = set(checkarray)
        if(int(len(converted)) == 14):
            part2_solution = i
            break
    sollution_List.pop(0)
    sollution_List.append("0")
print("Die Lösung für Part Zwei ist : " +  str( part2_solution))






6




## solution ermitteln
