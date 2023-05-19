def make_request(keys, values):
    new_dict = {}
    if len(keys) != len(values):
        return new_dict
    i = 0
    while i < len(keys):
        new_dict[keys[i]] = values[i]
        i += 1
    return new_dict


print(make_request(['one', 'two'], [1,2]))