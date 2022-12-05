import copy
lines = []
with open("2022/Day5_input_Moves.txt") as f:
    lines = f.readlines()

## Daten aufbereiten Moves
moves = []
for ele in lines:
    ele = ele.replace("\n", "")
    ele = ele.replace("move", "")
    ele = ele.replace("from", "x")
    ele = ele.replace("to",  "x")
    ele = ele.replace(" ", "")
    moves.append(ele.split("x"))


## Daten aufbereiten Plan
with open("2022/Day5_input_plan.txt") as f:
    plan = f.readlines()
plantable = []
for ele in plan:
    ele = ele.replace("\n", "")
    ele = ele.replace(" ", "")
    
    plantable.append(ele.split(","))

counter = 0
##Array umdrehen

for ele in plantable:
    ele = ele.reverse()
part2 = copy.deepcopy(plantable)
## Moves sind im 2D Array moves, Plan ist im 2 D Array plantable
for ele in moves:
    ## 1 Wert Menge
    ## 2 Werte Von Wo
    ## 3 Wert Wohin? 
    quantity =int( ele[0])
    source = int(ele[1])
    sink = int(ele[2])
    
    for i in range(quantity):
   
        plantable[sink -1].append(plantable[source-1].pop())
    
   

solution = ""

##Part2
needed = []
for ele in moves:
    quantity =int( ele[0])
    source = int(ele[1])
    sink = int(ele[2])
    for i in range(quantity):

        needed.append( part2[source-1].pop())
        needed.reverse
    
        if( i == quantity-1):
            for i in range(int(len(needed))):
                part2[sink-1].append(needed.pop())
for ele in part2:
    solution += ele.pop()
print(solution)