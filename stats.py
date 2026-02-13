def count_words(text):
    return len(text.split())

def count_characters(characters):
    sorted_characters = {}
    characters_to_count = list(characters.lower())
    for character in characters_to_count:
        if character not in sorted_characters:
            sorted_characters[character] = 0
        sorted_characters[character] += 1
    return sorted_characters