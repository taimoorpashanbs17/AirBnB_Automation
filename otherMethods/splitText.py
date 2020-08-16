
def format_text(text, index):
    if " · " in text:
        split_string = text.split(" · ", 1)
        substring = split_string[index]
        return substring
    else:
        return text
