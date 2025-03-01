# Get user input
string = str(input('Enter a string: '))

# Initialize counters
vowel_count = 0
consonant_count = 0
vowels = set('aeiouAEIOU')

# Single-pass iteration
for char in str(string):
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Display counts
print(f"The number of vowels: {vowel_count}")
print(f"The number of consonants: {consonant_count}")
