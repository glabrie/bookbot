 
def word_count(text):
    return len(text.split())

def char_count(text):
    low_text = text.lower()
    characters = {}
    for i in low_text:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    return characters


def sort_dict(characters):
    char_list = [{"char": char, "num": count} for char, count in characters.items()]
    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list



