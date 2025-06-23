try:
    n = int(input("Enter how many numbers: "))
    Num = [int(input(f"Enter number {i + 1}: ")) for i in range(n)]
    max_num = Num[0]
    second_max = Num[1]

    for i in Num:
        if i > max_num:
            second_max = max_num
            max_num = i
    print(second_max)
except ValueError:
    print("Enter valid integers.")
