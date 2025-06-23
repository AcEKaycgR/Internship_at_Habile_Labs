try:
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Sum of even numbers:", sum(x for x in nums if x % 2 == 0))
except ValueError:
    print("Please enter valid integers.")
