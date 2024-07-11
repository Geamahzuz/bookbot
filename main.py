def count_char(text):
    char_count = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    text = text.lower()
    for char in text:
        if char in char_count:
            char_count[char] += 1
    return char_count


def get_sorted_list(dict):

    list = []
    for key in dict:
        list.append({"char": key, "num": dict[key]})

    def sort_on(dict):
        return dict["num"]

    list.sort(reverse=True, key=sort_on)

    return list


with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    word_count = len(file_contents.split())
    char_dict = count_char(file_contents)
    #print(len(file_contents.split()))
    #print(get_sorted_list(char_dict))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document \n\n")
    for dict in get_sorted_list(char_dict):
        print(f" The '{dict['char']}' character was found {dict['num']} times")
    print("--- End report ---")
