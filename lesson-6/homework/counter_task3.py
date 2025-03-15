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
    """Read the content of 'sample.txt'. Create it if missing."""
    if not os.path.exists(FILENAME):
        create_file()
    with open(FILENAME, "r") as file:
        return file.read().lower()

def count_words(text):
    """Count word frequencies while ignoring punctuation and capitalization."""
    words = text.translate(str.maketrans("", "", string.punctuation)).split()
    return Counter(words), len(words)

def save_report(word_counts, total_words):
    """Save word count analysis to 'word_count_report.txt'."""
    with open(REPORT_FILE, "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n\n")
        file.write("Top 5 Words:\n")
        for word, count in word_counts.most_common(5):
            file.write(f"{word} - {count}\n")

    print(f"\nReport saved to '{REPORT_FILE}'.")

def display_results(word_counts, total_words):
    """Display total word count and top 5 words."""
    print(f"\nTotal words: {total_words}")
    print("\nTop 5 most common words:")
    for word, count in word_counts.most_common(5):
        print(f"{word} - {count} times")

def main():
    """Main function to process the file and display word statistics."""
    text = read_file()
    word_counts, total_words = count_words(text)

    display_results(word_counts, total_words)
    save_report(word_counts, total_words)

if __name__ == "__main__":
    main()
