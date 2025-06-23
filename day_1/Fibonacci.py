try:
    Num = int(input("Enter a number: "))
    a = 0
    b = 1
    for _ in range(Num):
        print(a, end=" ")
        a, b = b, a + b
except ValueError:
    print("Not the right format please enter in the format '1' ")
else:
    print("Unknown error please try again")

