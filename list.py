# list operations:

# reversing using loop

lst = [0,1,2,3,4,5,6,7,8,9]

def loop():
    lstRev = list()
    for i in range(9,-1,-1):
        lstRev.append(lst[i])
    print(lstRev)

def stack(n):
    if n <=0:
        print(lst[0])
        return 0
    else:
        print(lst[n])
        stack(n-1)


stack(9)
loop()
