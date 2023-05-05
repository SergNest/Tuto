def save_credentials_users(path, users_info):
    with open(path, 'wb') as file:
        for username, password in users_info.items():
            # Encode the string in utf-8 format
            user_info_str = f"{username}:{password}".encode('utf-8')
            # Write the encoded string to the file, followed by a newline character
            file.write(user_info_str + b'\n')

print(save_credentials_users('WorkWithFiles/output.bin',  {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}))