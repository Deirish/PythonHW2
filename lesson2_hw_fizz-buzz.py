fizz = int(input())
buzz = int(input())
n = int(input())
i = 1
while i <= n:
    if i % fizz == 0 and i % buzz == 0:
        print("FB", end = " ")
    elif i % fizz == 0:
        print("F", end = " ")
    elif  i % buzz == 0:
        print("B", end = " ")
    else:
        print(i, end = " ")
    i+=1
