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
    n = len(data)
    i = 0

    while i < n:
        byte = data[i]

        if (byte >> 3) == 0b11110:
            num_bytes = 4
        elif (byte >> 4) == 0b1110:
            num_bytes = 3
        elif (byte >> 5) == 0b110:
            num_bytes = 2
        elif (byte >> 7) == 0b0:
            num_bytes = 1
        else:
            return False

        if i + num_bytes > n:
            return False

        for j in range(1, num_bytes):
            if (data[i + j] >> 6) != 0b10:
                return False

        i += num_bytes

    return True
