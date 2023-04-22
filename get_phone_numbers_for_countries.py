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
    UA_list = []
    JP_list = []
    TW_list = []
    SG_list = []
    country_code = {"UA": '380',
                    "JP": '81',
                    "TW": '886',
                    "SG": '65'}
    
    for phone in list_phones:
       new_phone = sanitize_phone_number(phone)
