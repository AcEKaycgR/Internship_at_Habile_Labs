try:
    n = int(input("Enter n: "))
    for num in range(2, n + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
    print()
except ValueError:
    print("Please enter a valid number.")
