Num = int(input("Enter a number: "))


def count(n):
    n = abs(n)
    digit_count = 0
    if n == 0:
        return 1
    while n > 0:
        n = n // 10
        digit_count += 1
    return digit_count


print(count(Num))
