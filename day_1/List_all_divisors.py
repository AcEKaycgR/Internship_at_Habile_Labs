try:
    Num = int(input("Enter a number: "))

    for i in range(1, Num + 1):
        if Num % i == 0:
            print(i)
except ValueError:
    print("Please enter a valid number.")
