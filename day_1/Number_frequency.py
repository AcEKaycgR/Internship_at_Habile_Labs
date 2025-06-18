Nums = list(map(int, input("Enter a number: ").split()))
x = int(input("Number to check: "))
count = sum(1 for i in Nums if i == x)
print(count)
