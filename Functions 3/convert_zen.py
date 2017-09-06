# import this
#
# def decode_zen_of_python():
#
#     zen_decoder = this.d
#     coded_zen = this.s
#     print coded_zen
#
#     decoded_chars = convert_chars(coded_zen, zen_decoder)
#
#     for char in coded_zen:
#         if char.isalpha():
#             decoded_chars.append(zen_decoder[char])
#         else:
#             decoded_chars.append(char)
#
#     decoded_text = ''.join(decoded_chars)
#     print '\n' + decoded_text
#
# decode_zen_of_python()

import this

def convert_chars(str_to_convert, decoder):

    decoded_chars = []

    for char in str_to_convert:
        if char.isalpha():
            decoded_chars.append(decoder[char])
        else:
            decoded_chars.append(char)

    return decoded_chars


def decode_zen_of_python():

    zen_decoder = this.d
    coded_zen = this.s
    print coded_zen

    decoded_chars = convert_chars(coded_zen, zen_decoder)

    decoded_text = ''.join(decoded_chars)
    print '\n' + decoded_text


decode_zen_of_python()
