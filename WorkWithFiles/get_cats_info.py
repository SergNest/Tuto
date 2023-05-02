def get_cats_info(path):
    list_ret = []
    with open(path) as fh:
        while True:       
          line = fh.readline() 
          if not line:
            break
            
          list_ret.append({"id": line.rsplit('\n')[0].rsplit(',')[0], "name": line.rsplit('\n')[0].rsplit(',')[1], "age": line.rsplit('\n')[0].rsplit(',')[2]},)
    return list_ret


print(get_cats_info('WorkWithFiles/test.txt'))

 #.rsplit(',')