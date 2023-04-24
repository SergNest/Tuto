def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    
    country_code = {"UA": '380',
                    "JP": '81',
                    "TW": '886',
                    "SG": '65'}
    
    return_code = {"UA": [],
                "JP": [],
                "TW": [],
                "SG": []}
    
    for phone in list_phones:
       new_phone = sanitize_phone_number(phone)
       for code in country_code:
        check = new_phone.removeprefix(country_code.get(code))
        if len(check) != len(new_phone):
           return_code[code].append(new_phone)
           break
       else: 
        return_code['UA'].append(new_phone)
    return return_code


print(get_phone_numbers_for_countries(['380998759405', '818765347', '8867658976', '657658976']))