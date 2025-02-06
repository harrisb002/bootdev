def count_words(book):
    return len(book.split())


def num_of_characters(book):
    return len(book)


def number_of_occurences(book):
    char_dict = {}

    for char in book:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
            continue

        char_dict[char] += 1

    return char_dict


def get_report(char_dict):
    # ASCII a: 61 - z: 122
    report = ""
    for key in char_dict:
        if 61 <= ord(key) <= 122:
            report += f"The '{key}' character was found {char_dict[key]} times\n"
    return report


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    num_of_words = count_words(file_contents)
    num_of_chars = num_of_characters(file_contents)
    char_dict = number_of_occurences(file_contents)
    report = get_report(char_dict)

    print(report)


if __name__ == "__main__":
    main()
