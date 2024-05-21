#!/usr/bin/python3
""" checks if a given list of bytes represents a valid UTF-8 encoding """


def validUTF8(data):
    """
    The function `validUTF8` checks if a given list of bytes represents a valid UTF-8 encoding.

    :param data: It seems like you have provided the code snippet for a function that checks if a given
    byte array represents a valid UTF-8 encoding. However, you have not provided the actual data that
    you want to check using this function. Could you please provide the byte array data so that I can
    assist you further
    :return: The function `validUTF8` returns a boolean value - `True` if the input `data` is a valid
    UTF-8 encoding, and `False` otherwise.
    """
    number_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:
        mask_byte = 1 << 7

        if number_bytes == 0:
            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & mask_1 and not (i & mask_2)):
                return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
