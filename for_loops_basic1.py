for x in range(0,151):
    print(x)

for x in range(0,151,5):
    print(x)

for x in range(0,101):
    if x % 10 == 0:
        print("coding dojo")
    elif x % 5 == 0:
        print("coding")
    else:
        print(x)

sum = 0
for x in range(1,500001,2):
    sum += x
print(sum)
#62500000000 baybeeeeeeee!!!!!!!!!!!!!!!!!!!!!!!!!

for x in range(2018,0,-4):
    print(x)

lowNum = 2
highNum = 9
mult = 3

for x in range(lowNum,highNum + 1):
    if x % mult == 0:
        print(x)