message = "Hello my little friends!"
offset = int(37)
encoded_message = ""

for ch in message:
    if not ch.isalpha():
        new_char = ch
    else:
        case = 65 if ch.isupper() else 97
        possition = ord(ch) - case
        new_possition = (possition + offset) % 26
        new_char = chr(new_possition + case)
    encoded_message += new_char
print(encoded_message)
