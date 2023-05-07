import base64


def encode_data_to_base64(data):
    l_return = []
    for username in data:
        message_bytes = username.encode('utf-8')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode("utf-8")
        l_return.append(base64_message)
    return l_return

print(encode_data_to_base64({'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}))