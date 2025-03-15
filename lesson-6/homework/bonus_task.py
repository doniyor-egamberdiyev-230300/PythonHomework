import os
import string
from collections import Counter

FILENAME = "sample.txt"
REPORT_FILE = "word_count_report.txt"

def create_file():
    """Prompt the user to create 'sample.txt' if it doesn't exist."""
    text = input("File not found. Enter a paragraph to create 'sample.txt':\n")
    with open(FILENAME, "w") as file:
        file.write(text)
    print("File created successfully.")

def read_file():
    """Read the content of 'sample.txt' efficiently (line by line)."""
    if not os.path.exists(FILENAME):
        create_file()
    words = []
    with open(FILENAME, "r", encoding="utf-8") as file:
        for line in file:
            words.extend(line.lower().translate(str.maketrans("", "", string.punctuation)).split())
    return words

def count_words(words):
    """Count word frequencies while ignoring punctuation and capitalization."""
    return Counter(words), len(words)

def save_report(word_counts, total_words, top_n):
    """Save word count analysis to 'word_count_report.txt'."""
    with open(REPORT_FILE, "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n\n")
        file.write(f"Top {top_n} Words:\n")
        for word, count in word_counts.most_common(top_n):
            file.write(f"{word} - {count}\n")

    print(f"\nReport saved to '{REPORT_FILE}'.")

def display_results(word_counts, total_words, top_n):
    """Display total word count and top N most common words."""
    print(f"\nTotal words: {total_words}")
    print(f"\nTop {top_n} most common words:")
    for word, count in word_counts.most_common(top_n):
        print(f"{word} - {count} times")

def main():
    """Main function to process the file and display word statistics."""
    words = read_file()
    if not words:
        print("The file is empty. Please enter text into 'sample.txt'.")
        return

    try:
        top_n = int(input("Enter the number of top common words to display: "))
        if top_n <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    word_counts, total_words = count_words(words)

    display_results(word_counts, total_words, top_n)
    save_report(word_counts, total_words, top_n)

if __name__ == "__main__":
    main()
