try:
    nums = [int(input(f"Enter number {i + 1}: ")) for i in range(5)]
    print("Maximum:", max(nums))
except ValueError:
    print("Enter only valid integers.")
