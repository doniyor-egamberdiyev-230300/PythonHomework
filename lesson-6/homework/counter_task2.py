import os
import string
from collections import Counter

FILENAME = "sample.txt"

def create_file():

    text = input("File not found. Enter a paragraph to create 'sample.txt':\n")
    with open(FILENAME, "w") as file:
        file.write(text)
    print("File created successfully.")

def read_file():

    if not os.path.exists(FILENAME):
        create_file()
    with open(FILENAME, "r") as file:
        return file.read().lower()

def count_words(text):

    words = text.translate(str.maketrans("", "", string.punctuation)).split()
    return Counter(words)

def main():

    text = read_file()
    word_counts = count_words(text)

    print("\nWord Frequency Count:")
    for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
