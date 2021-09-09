def get_summ(one, two, delimiter='&'):
    some_string = f"{one}, {delimiter}, {two}".upper()
    return some_string
print(get_summ('Learn', 'python'))