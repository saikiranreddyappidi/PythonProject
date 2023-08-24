def right_shift_zero_fill(number):
    return number >> 8


def right_shift_sign_extension(number):
    if number & 0x8000:  # If the leftmost bit is 1 (i.e., number is negative)
        return (number >> 8) | 0xFF00  # Fill the leftmost 8 bits with 1
    else:
        return number >> 8


def left_shift(number):
    return number << 8


def left_rotate(number):
    return ((number << 8) | (number >> 8)) & 0xFFFF


def right_rotate(number):
    return ((number >> 8) | (number << 8)) & 0xFFFF


# Sample 16-bit binary number
num = 0b1100110011001100

# Testing the ALU operations on the sample number
print("Original number:", bin(num))
print("Right shift with zero fill:", bin(right_shift_zero_fill(num)))
print("Right shift with sign extension:", bin(right_shift_sign_extension(num)))
print("Left shift:", bin(left_shift(num)))
print("Left rotate:", bin(left_rotate(num)))
print("Right rotate:", bin(right_rotate(num)))
