def get_binary_from_int(num_int, bit_size=9):
    if bit_size > 0 and (num_int < 0 or num_int >= 2 ** bit_size):
        raise ValueError("num_int must fit in bit_size bits")
    return format(num_int, "b").zfill(bit_size)
