def Factorial(n):
    if n == 1:
        return 1
    else:
        return n * Factorial(n - 1)


Num = int(input("Enter a number: "))
print(Factorial(Num))
