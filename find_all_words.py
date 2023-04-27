import re


def replace_spam_words(text, spam_words):   
    
    for word in spam_words:
        
        regex_name = re.compile(word, re.IGNORECASE)  
        res = regex_name.findall(text)
        
        for el in res:
            text = re.sub(el, "*" * len(el) , text)

    return text


print(replace_spam_words(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    ["Python", "began", ]))
