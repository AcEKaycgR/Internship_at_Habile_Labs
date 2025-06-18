nums = list(map(int, input("Enter numbers separated by space").split()))
unique = []
for num in nums:
    if num not in unique:
        unique.append(num)
print(unique)
