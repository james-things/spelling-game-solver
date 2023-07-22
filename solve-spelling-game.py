import sys
import itertools

def load_words(file_path):
    with open(file_path, 'r') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

def find_words(mandatory, optionals, words):
    valid_chars = set(mandatory + ''.join(optionals))
    valid_words = [word for word in words if set(word).issubset(valid_chars) and mandatory in word and len(word) >= 4]
    valid_words.sort(key=len, reverse=True)
    return valid_words

def solve_game(mandatory, optionals):
    words = load_words('english_words.txt')
    return find_words(mandatory, optionals, words)

def print_in_columns(words, num_cols):
    if not words:
        return
    split_words = itertools.zip_longest(*(iter(words),) * num_cols)
    max_len = len(max(words, key=len))
    for column in split_words:
        column = [word if word is not None else '' for word in column]  # Replace None items with empty strings
        line = ''.join(word.ljust(max_len + 2) for word in column)  # Add 2 spaces for padding between columns
        print(line)

def main():
    while True:
        print("Welcome to the spelling game solver!\n")
        mandatory = input("Please enter the center letter: ")
        optionals = list(input("Please enter the 6 surrounding letters (no spaces): "))
        words = solve_game(mandatory, optionals)
        print(f'\nPotentially valid words are:\n')
        print_in_columns(words, 10)
        print(f'\nPlease note that obscure or inappropriate words are likely to be rejected.\n')

        continue_game = input("Would you like to solve another board? (y/n): ")
        if continue_game.lower() != 'y':
            break
        else:
            print("")

if __name__ == "__main__":
    main()
