def is_spam_words(text, spam_words, space_around=False):
    new_text = text.replace(".", "").replace(",", "")

    if space_around:
        list_text = new_text.split(" ")
        for el in spam_words:
            for word in list_text:
                if el == word:
                    return True
    else:
        for el in spam_words: 
            if el in new_text:
                return True
    
    return False

print(is_spam_words("Ты хорош, но выглядишь как лох.", ["лох"], True))