def get_num_words(text):
    words = text
    return len(words.split())

def num_of_characters(text):
    chars = {}
    for c in text:
        lower_char = c.lower()
        if lower_char in chars:
            chars[lower_char] += 1
        else:
            chars[lower_char] = 1
    return chars

def sort_on(items):
    return items["num"]

def sort_chars(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list