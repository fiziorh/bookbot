book_path = "books/frankenstein.txt"

def read_text():
    text = get_book(book_path)
    print(text)

def count_words():
    i = 0
    text = get_book(book_path)
    words = text.split()
    for word in words:
        i+=1
    print(i)

def get_book(path):
    with open(path) as f:
        return f.read()

read_text()
count_words()