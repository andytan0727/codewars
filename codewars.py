import string

def alphabet_position(text):
    uppercase_alphabet = string.uppercase
    lowercase_alphabet = string.lowercase
    alphabet_pos = []

    for char in text:
        if char in uppercase_alphabet:
            alphabet_pos.append(str(ord(char) - 64))
        elif char in lowercase_alphabet:
            alphabet_pos.append(str(ord(char) - 96))
        else:
            continue

    return ' '.join(alphabet_pos)

print alphabet_position("The sunset sets at twelve o' clock.")
