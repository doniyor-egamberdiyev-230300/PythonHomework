sentence = input("Enter a sentence: ").strip()

words = sentence.split()
if words:
    start_word = words[0]
    end_word = words[-1]
    print(f"The sentence starts with '{start_word}' and ends with '{end_word}'.")
else:
    print("The sentence is empty.")