import re


# def find_all_emails(text):
#     pattern = r'\b[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}\b'
#               r'\b(?!.*\d.*@)[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}\b'
              
#     result = re.findall(pattern, text)
#     return result

def find_all_emails(text):
    pattern = r'(?!\d)[A-Za-z][\w.]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)


# ['['Ima.Fool@iana.org',                'first_last@iana.org', 'first.middle.last@iana.or', 'abc111@test.com']
# ['Ima.Fool@iana.org', 'Fool@iana.org', 'first_last@iana.org', 'first.middle.last@iana.or', 'abc111@test.com']
# 
print(find_all_emails('Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net' ))