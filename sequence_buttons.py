
def sequence_buttons(string):
    button_map = {
        '1': '.?,!:',
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ',
        '0': ' '
    }
   
    sequence = ''
    for char in string:
        char = char.upper()
        if char == ' ':
            sequence += '0'
        else:
            for button, characters in button_map.items():
                if char in characters:
                    sequence += button * (characters.index(char) + 1)
                    break

    return sequence


text = "Hi there!"
result = sequence_buttons(text)
print(result)