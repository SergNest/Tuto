import re


def find_word(text, word):
    sword = word.lower()   
    regex_name = re.compile(sword, re.IGNORECASE)  
    # res = regex_name.findall(text)
    return regex_name.findall(text)


print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))
