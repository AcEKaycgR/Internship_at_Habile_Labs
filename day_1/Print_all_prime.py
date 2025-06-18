Num = int(input("Enter a number: "))
for x in range(2, Num + 1):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            break
    else:
        print(x, end=" ")
