try:
    word = input("Enter a word: ").lower()
    vowels = "aeiou"
    count = sum(1 for ch in word if ch in vowels)
    print("Vowel count:", count)
except Exception as e:
    print("Error:", e)
