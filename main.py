import sys
def sys_check():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
from stats import get_num_words, get_chars_dict, get_report
def get_book_text(path):
    with open(path) as f:
        return f.read()
def main():
    sys_check()
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    char_dict = get_chars_dict(book_text)
    report=get_report(char_dict)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {sys.argv[1]}')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for item in report:
        print(f"{item['char']}: {item['count']}")
    print('============= END ===============')
main()