# Input: List of Marks
# Expected: Print whether marks is low, medium or high. Low = <10, medium 10-70, high >70

m = [20, 4, 80, 69, 100]

for item in m:
    if item < 10:
        if item < 5:
            print("very low")
        else:
            print("low")
    elif item>10 and item<70:
        print("medium")
    else:
        print("high")



name = "Amuthan"
if name  == "Amuthan":
    print("Yes")


# Input: List of Names
# Expected: If name's first letter startswith 'A' print 1, if first letter startswith 'M' print 2,
# if anyother letter , if second leter startswith 'A' print 3, else print 4

'AMUTHAN' -> 1
'MANI' -> 2
'CAT' -> 3
'DOG' -> 4

N =['AMUTHAN','MANI','CAT','DOG']
for name in N:
        if name[0].startswith('A'):
            print(1)
        elif name[0].startswith('M'):
            print(2)
        elif name[1].startswith('A'):
            print(3)
        else:
            print(4)


