word = input("Enter the word: ")
vowels = "aeiouAEIOU"

count = 0
for character in word:
    if character in vowels:
        count += 1

print(count)
