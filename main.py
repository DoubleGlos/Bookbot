def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    path_to_book = "books/frankenstein.txt"
    print(get_book_text(path_to_book))

main()