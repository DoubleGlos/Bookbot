import sys
from stats import count_words, count_characters, create_report

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
  
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]
    book_text = get_book_text(path_to_book)
    num_words = count_words(book_text)
    num_characters = count_characters(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_chars = create_report(num_characters)
    for entry in sorted_chars:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")

main()