import sys
from stats import get_num_words, get_num_characters, get_dictionary_to_sorted

args = sys.argv
script = sys.argv[0]

if len(sys.argv) < 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)


def get_book_text(path_to_file):
  with open(path_to_file) as f:
   file_contents = f.read()
   return file_contents

def main():
  book = get_book_text(args[1])
  num_words = get_num_words(book)
  num_characters = get_num_characters(book)
  unsorted_characters = get_dictionary_to_sorted(num_characters)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {args[1]}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for i in range(0, len(unsorted_characters)):
    if unsorted_characters[i]["char"].isalpha():
       print(f"{unsorted_characters[i]['char']}: {unsorted_characters[i]['num']}")
  print("============= END ===============")
main()
