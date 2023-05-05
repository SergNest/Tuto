def is_equal_string(utf8_string, utf16_string):
    utf8 = utf8_string.decode('utf-8')
    utf16 = utf16_string.decode('utf-16')
    return utf8 == utf16