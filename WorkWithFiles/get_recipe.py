def get_recipe(path, search_id):
    list_ret = []
    with open(path) as fh:
        while True:       
          line = fh.readline() 
          if not line:
            break
          list_line = line.rsplit('\n')[0].rsplit(',')  
          list_ret.append({"id": list_line[0], "name": list_line[1], "ingredients": [list_line[2],list_line[3],list_line[4]]},)
        for el in list_ret:
           if el.get('id') == search_id:
              return el

    return None


print(get_recipe('WorkWithFiles/test.txt', "60b90c3b13067a15887e1ae4"))