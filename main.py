def read_contents_from_file(filepath):
    with open(filepath) as file:
        return file.read()
    
def count_words_in_string(string):
    split_string_as_list = string.split()
    return len(split_string_as_list)

def count_letters_in_string(string):
    letter_count = {}
    lowercase_string = string.lower()
    for letter in lowercase_string:
        if letter not in letter_count:
            letter_count[letter] = 0
        letter_count[letter] += 1
    return letter_count

def main():
    frankenstein = read_contents_from_file("books/frankenstein.txt")
    frankenstein_word_count = count_words_in_string(frankenstein)
    frankenstein_letter_count = count_letters_in_string(frankenstein)
    print(f"{frankenstein_word_count} words found in the document.")
    print(frankenstein_letter_count)

main()