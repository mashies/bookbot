def read_contents_from_file(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents
    
def main():
    frankenstein = read_contents_from_file("books/frankenstein.txt")
    print(frankenstein)

main()