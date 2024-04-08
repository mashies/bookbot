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

def sort_on(d):
    return d["num"]

def dictionary_sort(dictionary):
    sorted_result = []
    for item in dictionary:
        sorted_result.append({"character": item, "num": dictionary[item]})
    sorted_result.sort(reverse=True, key=sort_on)
    return sorted_result

def main():
    book_path = "books/frankenstein.txt"
    frankenstein = read_contents_from_file(book_path)
    frankenstein_word_count = count_words_in_string(frankenstein)
    frankenstein_letter_count = count_letters_in_string(frankenstein)
    frankenstein_letter_count_sorted = dictionary_sort(frankenstein_letter_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{frankenstein_word_count} words found in the document")
    print()

    for item in frankenstein_letter_count_sorted:
        if not item["character"].isalpha():
            continue
        print(f"The '{item['character']}' character was found {item['num']} times.")

    print("--- End report ---")

main()