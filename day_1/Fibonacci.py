Num = int(input("Enter a number: "))
a = 0
b = 1
for _ in range(Num):
    print(a, end=" ")
    a, b = b, a + b
