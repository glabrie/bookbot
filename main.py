from stats import word_count, char_count, sort_dict
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
   
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
   
def main():
    text = get_book_text(sys.argv[1])
    num_words = word_count(text)
    char_count_result = char_count(text)
    alpha_characters = {char: count for char, count in char_count_result.items() if char.isalpha()}
    sorted_list = sort_dict(alpha_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        print(f"{entry['char']}: {entry['num']}")

main()

