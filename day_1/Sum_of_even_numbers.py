Nums = list(map(int, input("Enter all numbers: ").split()))
even_sum = sum(x for x in Nums if x % 2 == 0)
print(f"Even sum: {even_sum}")
