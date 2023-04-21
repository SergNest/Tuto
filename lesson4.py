articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles_2(key, letter_case=False):
    result = []
    for article in articles_dict:
        if letter_case:
            if key in article['title'] or key in article['author']:
                result.append(article)
        else:
            if key.lower() in article['title'].lower() or key.lower() in article['author'].lower():
                result.append(article)
    return result

def find_articles(key, letter_case=False):
    new_list = []
    
    for ldict in articles_dict:
        
        for val in ldict.values():
          
           if isinstance(val, str):
            words = val.split(" ")
            for i in words:
                scr =  i.find(key) if letter_case else i.lower().find(key if letter_case else key.lower()) 
                if scr > -1:
                    new_list.append(ldict)
                    break
    return new_list

print(find_articles('Ocean'))