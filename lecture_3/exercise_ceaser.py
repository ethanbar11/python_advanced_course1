import string


def move_letter(c, move_amount):
    letters = list(string.ascii_lowercase)
    c_as_lower = c.lower()
    if c_as_lower in letters:
        index_of_letter = letters.index(c_as_lower)
        new_index = (index_of_letter + move_amount) % len(letters)
        letter = letters[new_index]
        if c == c_as_lower:
            return letter
        else:
            return letter.upper()
    else:
        return c


def encode_line(s, move_amount):
    new_line = ''
    for c in s:
        new_line += move_letter(c, move_amount)
    return new_line
    # return str(map(lambda a: move_letter(a, move_amount), s))


def encode_file(file_path, file_path_to_write, move_amount):
    with open(file_path, 'r') as file_to_encode:
        with open(file_path_to_write, 'w') as file_to_write:
            for line in file_to_encode:
                encoded_line = encode_line(line, move_amount)
                file_to_write.write(encoded_line)


def get_encoded_file_name(file_name):
    lst = file_name.split('.')
    return lst[0] + '_encoded.' + lst[1]


def get_decoded_file_name(file_name):
    lst = file_name.split('.')
    return lst[0] + '_decoded.' + lst[1]


if __name__ == '__main__':
    file_name = input('Give me the file name please: ')
    is_for_encoding = input('Is it for encoding? 1/2') == '1'
    move_amount = int(input('Insert move amount: '))
    if is_for_encoding:
        file_name_to_write = get_encoded_file_name(file_name)
        encode_file(file_name, file_name_to_write, move_amount)
    else:
        file_name_to_write = get_decoded_file_name(file_name)
        encode_file(file_name, file_name_to_write, -move_amount)
