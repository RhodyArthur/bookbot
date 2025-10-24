import sys
from stats import get_num_words
from stats import get_num_chars
from stats import print_sorted_report

def get_book_text(path_to_file):
    try:
        with open(path_to_file) as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        raise FileNotFoundError("File not found: " + path_to_file)
    

def main():
    if len(sys.argv) > 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    book_string = get_book_text(path_to_book)
    
    print (f"""
    ============ BOOKBOT ============
    Analyzing book found at books/frankenstein.txt...
    ----------- Word Count ----------
    {get_num_words(book_string)}
    --------- Character Count -------
    {print_sorted_report(get_num_chars(book_string))}
    ============= END ===============
    """)
    
main()