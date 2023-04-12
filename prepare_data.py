
def prepare_data(data):
    new_num = sorted(data)
    return new_num[1:-1]


print(prepare_data([1, 3.1415, 41, 3]))
