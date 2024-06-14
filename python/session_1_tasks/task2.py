def isVowel(letter):
    vowels = ('a', 'i', 'e', 'o', 'u')
    if letter in vowels:
        return True
    else:
        return False

print(f"Is g vowel? {isVowel('g')}")
print(f"Is a vowel? {isVowel('a')}")


