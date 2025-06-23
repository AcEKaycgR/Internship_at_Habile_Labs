try:
    n = int(input("Enter an integer: "))
    print("Even" if n % 2 == 0 else "Odd")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
