from stats import get_num_words

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        

        character_counts = count_characters(text)
        

        sorted_characters = sort_characters(character_counts)
        
        print(f"--- Begin report of {book_path} ---")
        print(f"{num_words} words found in the document")
        print()

        for char_dict in sorted_characters:
            char = char_dict["char"]
            count = char_dict["num"]
            print(f"{char}: {count}")

        print("--- End report ---")
    
def get_book_text(path):
    with open(path) as f:
        return  f.read()
    
def count_characters(text):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in characters:
                characters[lowered] += 1
            else:
                characters[lowered] = 1
    return characters

def sort_characters(characters):
    list_dict = []
    for char, count in characters.items():
        char_dict = {"char" : char, "num" : count}
        list_dict.append(char_dict)
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict

def sort_on(element):
    return element["num"]

main()