# ChatGPT-3.5 generated version 12.11.2023

import argparse

def read_words_from_file(file_path, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            lines = file.read().splitlines()
        words_dict = {line.split(';')[0]: line.split(';')[1] for line in lines}
        return words_dict
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}

def quiz(words_dict):
    correct_count = 0
    total_words = len(words_dict)

    for word, translation in words_dict.items():
        user_translation = input(f"What is the translation of '{word}'? ").strip().lower()

        if user_translation == translation.lower():
            print("Correct!\n")
            correct_count += 1
        else:
            print(f"Wrong! The correct translation is '{translation}'.\n")

    print(f"You got {correct_count} out of {total_words} words correct.")

def main():
    parser = argparse.ArgumentParser(description='Language Quiz')
    parser.add_argument('file_path', type=str, help='Path to the word file')
    parser.add_argument('language', type=str, help='Language for the quiz')

    args = parser.parse_args()

    try:
        words_dict = read_words_from_file(args.file_path)
    except FileNotFoundError:
        print(f"Error: File for language '{args.language}' not found.")
        return

    if words_dict:
        print(f"Welcome to the {args.language} language quiz!\n")
        quiz(words_dict)
    else:
        print("No words found in the file.")

if __name__ == "__main__":
    main()

