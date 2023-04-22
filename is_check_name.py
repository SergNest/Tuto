def is_check_name(fullname, first_name):
    check = fullname.removeprefix(first_name)
    return first_name + check == fullname

is_check_name('Alex Old', 'Alex')