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

def create_report(sorted_characters):
    report = []
    for char, count in sorted_characters.items():
        report_entry = {"char":char , "num":count}
        report.append(report_entry)
    report.sort(reverse=True, key=sort_on)
    return report

def sort_on(items):
    return items["num"]