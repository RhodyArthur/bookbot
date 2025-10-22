def get_num_words(text):
    num_words = len(text.split())
    return f"Found {num_words} total words"

def get_num_chars(text):
    char_count = {}
    for char in text:
        char_lower = char.lower()
        if char_lower.isalpha():
            if char_lower in char_count:
                char_count[char_lower] += 1
            else:
                char_count[char_lower] = 1
    return char_count

def sort_on(item):
    return item['num']

def print_sorted_report(char_count_dict):
    items = []
    for key, value in char_count_dict.items():
        items.append({'char': key, 'num': value})
    items.sort(reverse=True, key=sort_on)
    lines = []
    for item in items:
        lines.append(f"{item['char']}: {item['num']}")
    return "\n".join(lines)