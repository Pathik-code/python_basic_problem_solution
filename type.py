


# if (False and True):
#     print('Yes')
# else:
#     print('No')
#     print(divmod(2,3))


# Example integers
x = 10  # binary: 1010
y = 4   # binary: 0100

# Bitwise OR
bitwise_or = x | y  # binary: 1110, decimal: 14
print(f"{x} | {y} = {bitwise_or}")

# Bitwise XOR
bitwise_xor = x ^ y  # binary: 1110, decimal: 14
print(f"{x} ^ {y} = {bitwise_xor}")

# Bitwise AND
bitwise_and = x & y  # binary: 0000, decimal: 0
print(f"{x} & {y} = {bitwise_and}")

# Left shift
left_shift = x << 2  # binary: 101000, decimal: 40
print(f"{x} << 2 = {left_shift}")

# Right shift
right_shift = x >> 2  # binary: 0010, decimal: 2
print(f"{x} >> 2 = {right_shift}")

# Bitwise NOT
bitwise_not = ~x  # binary: -1011, decimal: -11 (in two's complement)
print(f"~{x} = {bitwise_not}")
