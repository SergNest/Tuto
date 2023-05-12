
def prepare_data_simple(data):
    new_num = sorted(data)
    return new_num[1:-1]

def prepare_data(list_data):
    r_list = []
    for el in list_data:
        if len(el) > 2:
            new_num = sorted(el)[1:-1]
            r_list.extend(new_num)
        else:
            r_list.extend(el) 
        r_list.sort(reverse=True)
    return r_list



print(prepare_data([[1,2,3],[3,4], [5,6]]))
