def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        # a = ""
        # for i in range(length - len(string)):
        #     a += " "
        # return a + string
        num_spaces = (length - len(string)) // 2
        a = ' ' * num_spaces + string
        return a

a = format_string('aaab', 15)   
print(len(a))

print(11//2)