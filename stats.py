def get_book_word_count(book_text):
    return len(book_text.split())

def get_book_symbol_count(book_text):
    chars = {}
    for char in book_text:
        lower_case_char = char.lower()
        if lower_case_char in chars:
            chars[lower_case_char] += 1
        else:
            chars[lower_case_char] = 1
    return chars

def sort_on(dict):
    return dict["count"]

def get_book_sorted_symbols(symbol_count):
    list = []
    for key in symbol_count:
        list.append({
            "char": key,
            "count": symbol_count[key]
        })

    list.sort(reverse=True, key=sort_on)
    return list