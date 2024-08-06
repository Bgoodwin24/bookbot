def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text) 
    

    character_counts = count_characters(text)
    

    sorted_characters = sort_characters(character_counts)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()

    for char_dict in sorted_characters:
        char = char_dict["char"]
        count = char_dict["num"]
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")
    

def count_words(text):
    words = text.split()
    return len(words)
    
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