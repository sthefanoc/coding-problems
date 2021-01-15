def string_encoding(string):
    final_string = ''
    repetitions = 1
    curr_char = ''

    for i, char in enumerate(string):
        if char == curr_char:
            repetitions += 1
        else:
            if i != 0:
                final_string += str(repetitions) + curr_char
            curr_char = char
            repetitions = 1
        if i == len(string)-1:
            final_string += str(repetitions) + curr_char
    return final_string


def string_decoding(encoded_string):
    final_string = ''
    repetitions = ''
    for char in encoded_string:
        if char.isnumeric():
            repetitions += char
        else:
            final_string += char*int(repetitions)
            repetitions = ''
    return final_string


string = 'AAAABBBCCDAA'
encoded_string = '4A3B2C1D2A'


print(string_encoding(string))
print(string_decoding(encoded_string))
