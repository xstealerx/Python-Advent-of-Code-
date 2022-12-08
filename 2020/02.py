from locale import strcoll


passwörter = []

with open("02.txt") as f:
    passwörter = list(map(str, f.readlines()))

valid = 0
unvalid = 0

for ele in passwörter:
    ele = ele.split(":")
    ele[1] = ele[1].replace(" ", "")
    ele[1] = ele[1].replace("\n", "")
    letters = ele[0]
    letter = letters[-1]

    anzahl = ele[1].count(letter)
    ersteZahl = ele[0].split("-")
    zweiteZahl = ersteZahl[1].split(" ")
    minum = int(ersteZahl[0])
    maximum = int(zweiteZahl[0]) 
    password = ele[1]

    if password[minum -1] == letter and not password[maximum-1] != letter:
        valid = valid + 1
    elif password[maximum -1 ] == letter and not password[minum-1 ] != letter:
        valid = valid + 1
            
            

1

    # if(minum<= anzahl and anzahl <= maximum ):
    #    valid =  valid +1
    # else:
    #    unvalid = unvalid+1

print(valid, unvalid)
print(password, minum, maximum, anzahl, letters)

# 6-7 g: gghggcggg
