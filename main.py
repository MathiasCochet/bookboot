import sys
from stats import *

def main():
    arguments = sys.argv
    
    if len(arguments) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    book_text = get_book_text(book_path)

    word_count = get_book_word_count(book_text)
    
    symbol_count = get_book_symbol_count(book_text)
    sorted_symbols = get_book_sorted_symbols(symbol_count)

    print_report(book_path, word_count, sorted_symbols)


def get_book_text(file_path):
    with open (file_path) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, word_count, sorted_symbols):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")
    
    for symbol in sorted_symbols:
        char = symbol["char"]
        if char.isalpha():
            print(f"{char}: {symbol["count"]}")

    print("============= END ===============")


main()