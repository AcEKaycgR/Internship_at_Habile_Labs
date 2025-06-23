try:
    def prime(n):
        if n < 2:
            return "Not Prime"
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return "Not prime"
                else:
                    return "Prime"


    Num = int(input("Enter a number: "))
    print(prime(Num))
except ValueError:
    print("Please enter a valid integer.")
