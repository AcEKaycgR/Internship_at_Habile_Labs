word = input("Enter a word: ").lower()
vowels = "aeiou"
count = sum(1 for ch in word if ch in vowels)
print(f"Vowels in word is {count}")
