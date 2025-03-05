def to_base(n, base):
    if n == 0:
        return '0'
    digits = []
    while n > 0:
        digits.append(n % base)
        n = n // base
    return ''.join(str(d) for d in reversed(digits))

input_str = input().strip()
if not input_str.isdigit() or int(input_str) <= 0:
    print("Неверный ввод")
else:
    num = int(input_str)
    bin_num = to_base(num, 2)
    oct_num = to_base(num, 8)
    hex_digits = '0123456789ABCDEF'
    hex_num = ''
    temp = num
    while temp > 0:
        hex_num = hex_digits[temp % 16] + hex_num
        temp = temp // 16
    hex_num = hex_num if hex_num else '0'
    print(f"{bin_num}, {oct_num}, {hex_num}")