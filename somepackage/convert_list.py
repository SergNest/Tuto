import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    if isinstance(cats[0], dict):
        llist = []
        for k in cats:
            cat = Cat(k.get("nickname"), k.get("age"), k.get("owner"))
            llist.append(cat)
        return llist
    else:
        llist = []
        for k in cats:
           ldict = {}
           ldict.update(nickname = k.nickname, age = k.age, owner = k.owner) 
           llist.append(ldict)
        return llist    

def convert_list(cats):
    if isinstance(cats[0], dict):  # перетворення зі списку словників в список іменованих кортежів
        return [Cat(cat["nickname"], cat["age"], cat["owner"]) for cat in cats]
    else:  # перетворення зі списку іменованих кортежів в список словників
        return [{"nickname": cat.nickname, "age": cat.age, "owner": cat.owner} for cat in cats]


# convert_list([
#     {"nickname": "Mick", "age": 5, "owner": "Sara"},
#     {"nickname": "Barsik", "age": 7, "owner": "Olga"},
#     {"nickname": "Simon", "age": 3, "owner": "Yura"},
# ])

convert_list([Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")])