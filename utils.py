def get_binary_from_int(num_int, bit_size=9):
    return format(num_int, "b").zfill(bit_size)