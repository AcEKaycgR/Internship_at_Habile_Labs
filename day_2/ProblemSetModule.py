import math
import random


class ProblemSet:

    @staticmethod
    def even_or_odd():
        try:
            n = int(input("Enter an integer: "))
            print("Even" if n % 2 == 0 else "Odd")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    @staticmethod
    def sum_of_n():
        try:
            n = int(input("Enter a number: "))
            print("Sum:", sum(range(1, n + 1)))
        except ValueError:
            print("Please enter a valid number.")

    @staticmethod
    def find_max():
        try:
            nums = [int(input(f"Enter number {i + 1}: ")) for i in range(5)]
            print("Maximum:", max(nums))
        except ValueError:
            print("Enter only valid integers.")

    @staticmethod
    def fizzbuzz():
        try:
            for i in range(1, 51):
                if i % 3 == 0 and i % 5 == 0:
                    print("FizzBuzz")
                elif i % 3 == 0:
                    print("Fizz")
                elif i % 5 == 0:
                    print("Buzz")
                else:
                    print(i)
        except Exception as e:
            print("Unexpected error:", e)

    @staticmethod
    def count_vowels():
        try:
            word = input("Enter a word: ").lower()
            vowels = "aeiou"
            count = sum(1 for ch in word if ch in vowels)
            print("Vowel count:", count)
        except Exception as e:
            print("Error:", e)

    @staticmethod
    def factorial():
        try:
            n = int(input("Enter a number: "))
            print("Factorial:", math.factorial(n))
        except ValueError:
            print("Enter a non-negative integer.")

    @staticmethod
    def reverse_number():
        try:
            n = input("Enter a number: ")
            print("Reversed:", n[::-1])
        except Exception as e:
            print("Error:", e)

    @staticmethod
    def print_triangle():
        try:
            n = int(input("Enter number of rows: "))
            for i in range(1, n + 1):
                print("*" * i)
        except ValueError:
            print("Please enter a valid integer.")

    @staticmethod
    def check_prime():
        try:
            n = int(input("Enter a number: "))
            if n < 2:
                print("Not prime")
            else:
                for i in range(2, int(n ** 0.5) + 1):
                    if n % i == 0:
                        print("Not prime")
                        return
                print("Prime")
        except ValueError:
            print("Please enter a valid integer.")

    @staticmethod
    def guess_number():
        try:
            secret = random.randint(1, 100)
            while True:
                guess = int(input("Guess the number (1–100): "))
                if guess < secret:
                    print("Too low!")
                elif guess > secret:
                    print("Too high!")
                else:
                    print("Correct!")
                    break
        except ValueError:
            print("Enter a valid number between 1–100.")

    @staticmethod
    def palindrome_checker():
        try:
            word = input("Enter a word: ").lower()
            print("Palindrome" if word == word[::-1] else "Not a palindrome")
        except Exception as e:
            print("Error:", e)

    @staticmethod
    def count_digits():
        try:
            n = input("Enter an integer: ")
            print("Number of digits:", len(n.lstrip('-')))
        except Exception as e:
            print("Error:", e)

    @staticmethod
    def multiplication_table():
        try:
            n = int(input("Enter a number: "))
            for i in range(1, 11):
                print(f"{n} x {i} = {n * i}")
        except ValueError:
            print("Please enter a valid integer.")

    @staticmethod
    def list_divisors():
        try:
            n = int(input("Enter a number: "))
            print("Divisors:", [i for i in range(1, n + 1) if n % i == 0])
        except ValueError:
            print("Please enter a valid number.")

    @staticmethod
    def second_largest():
        try:
            nums = list(map(int, input("Enter numbers separated by space: ").split()))
            unique = list(set(nums))
            unique.sort()
            print("Second largest:", unique[-2] if len(unique) >= 2 else "Not enough unique numbers")
        except ValueError:
            print("Enter valid integers.")

    @staticmethod
    def remove_duplicates():
        try:
            nums = list(map(int, input("Enter numbers separated by space: ").split()))
            print("Without duplicates:", list(dict.fromkeys(nums)))
        except ValueError:
            print("Enter valid numbers.")

    @staticmethod
    def fibonacci_sequence():
        try:
            n = int(input("Enter number of Fibonacci terms: "))
            a, b = 0, 1
            for _ in range(n):
                print(a, end=" ")
                a, b = b, a + b
            print()
        except ValueError:
            print("Enter a valid integer.")

    @staticmethod
    def sum_of_evens():
        try:
            nums = list(map(int, input("Enter numbers separated by space: ").split()))
            print("Sum of even numbers:", sum(x for x in nums if x % 2 == 0))
        except ValueError:
            print("Please enter valid integers.")

    @staticmethod
    def primes_up_to_n():
        try:
            n = int(input("Enter n: "))
            for num in range(2, n + 1):
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        break
                else:
                    print(num, end=" ")
            print()
        except ValueError:
            print("Please enter a valid number.")

    @staticmethod
    def frequency_in_list():
        try:
            nums = list(map(int, input("Enter list elements: ").split()))
            x = int(input("Enter number to count: "))
            print(f"{x} appears {nums.count(x)} times.")
        except ValueError:
            print("Please enter valid input.")


def run_cli():
    problems = {
        1: ("Even or Odd", ProblemSet.even_or_odd),
        2: ("Sum of N Numbers", ProblemSet.sum_of_n),
        3: ("Find Maximum in List", ProblemSet.find_max),
        4: ("FizzBuzz", ProblemSet.fizzbuzz),
        5: ("Count Vowels in a String", ProblemSet.count_vowels),
        6: ("Factorial", ProblemSet.factorial),
        7: ("Reverse a Number", ProblemSet.reverse_number),
        8: ("Print Triangle Pattern", ProblemSet.print_triangle),
        9: ("Check Prime Number", ProblemSet.check_prime),
        10: ("Guess the Number", ProblemSet.guess_number),
        11: ("Palindrome Checker", ProblemSet.palindrome_checker),
        12: ("Count Digits", ProblemSet.count_digits),
        13: ("Multiplication Table", ProblemSet.multiplication_table),
        14: ("List All Divisors", ProblemSet.list_divisors),
        15: ("Find Second Largest Number", ProblemSet.second_largest),
        16: ("Remove Duplicates from List", ProblemSet.remove_duplicates),
        17: ("Fibonacci Sequence", ProblemSet.fibonacci_sequence),
        18: ("Sum of Even Numbers in List", ProblemSet.sum_of_evens),
        19: ("Print All Prime Numbers up to N", ProblemSet.primes_up_to_n),
        20: ("Number Frequency in List", ProblemSet.frequency_in_list)
    }

    while True:
        print("\n=== Problem Menu ===")
        for num, (desc, _) in problems.items():
            print(f"{num}. {desc}")
        print("0. Exit")

        try:
            choice = int(input("Select an option (0-20): "))
            if choice == 0:
                print("Exiting... Goodbye!")
                break
            elif 1 <= choice <= 20:
                problems[choice][1]()
            else:
                print("Invalid choice. Please select a number between 0 and 20.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    run_cli()
