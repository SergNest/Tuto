def is_valid_password(password):
    if len(password) != 8:
        return False
    is_upper = False
    is_lower = False
    is_num = False
    for i in password:

        if not is_num:
            try:
                is_num = bool(int(i))
                continue
            except:
                pass

        if i.isupper() and i.isalpha():
            is_upper = True
        elif i.islower() and i.isalpha():
            is_lower = True

    return is_upper and is_lower and is_num


print(is_valid_password("b8g^ro4^"))
