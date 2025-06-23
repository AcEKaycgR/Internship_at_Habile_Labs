try:
    n = int(input("Enter a number: "))
    print("Sum:", sum(range(1, n + 1)))
except ValueError:
    print("Please enter a valid number.")
