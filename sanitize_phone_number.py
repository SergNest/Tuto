    # "    +38(050)123-32-34",
    # "     0503451234",
    # "(050)8889900",
    # "38050-111-22-22",
    # "38050 111 22 11   ",

def sanitize_phone_number(phone):
    clean = phone.strip()
    rstring = ''
    for el in clean:
        try:
           num = int(el)        
           rstring += el
        except:
            continue
    return rstring

def sanitize_phone_number2(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

print(sanitize_phone_number("(050)8889900")) 