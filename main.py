#Book path
book_path = "books/frankenstein.txt"

#Function
def main():
    print_list()

def read_text():
    text = get_book()
    print(text)

def count_words():
    text = get_book()
    words = text.split()
    return len(words)

def get_book():
    with open(book_path) as f:
        return f.read()

def get_chars_dict():
    chars = {}
    text = get_book()
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_chars_list():
    chars = get_chars_dict()
    sorted_list = []
    chars_list = list(chars.items())
    for i in range(0,len(chars_list)-1):
        if chars_list[i][0].isalpha()== True:
            sorted_list.append(chars_list[i])
    sorted_list = sorted(sorted_list, key=lambda x: x[1], reverse=True)
    return sorted_list

def print_list():
    sorted_list = get_chars_list()
    words = count_words()
    print(f"--- Begin report of {book_path} ---\n {words} words found in the document\n")
    for items in sorted_list:
        print(f"The '{items[0]}' character was found {items[1]} times\n")
    print("--- End report ---")
    



#Execute function
main()