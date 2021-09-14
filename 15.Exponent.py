
print(2**3)  # exponent

def raise_to_power(base_num, pow_num):
    result = 1
    for index4 in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 4))
