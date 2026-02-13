from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
  
def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    num_words = count_words(book_text)
    num_characters = count_characters(book_text)
    print(f"Found {num_words} total words")
    print(f"{num_characters}")

main()