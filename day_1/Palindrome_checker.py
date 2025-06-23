try:
    word = input("Enter a word: ").lower()
    print("Palindrome" if word == word[::-1] else "Not a palindrome")
except Exception as e:
    print("Error:", e)
