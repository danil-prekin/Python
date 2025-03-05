input_str = input().strip()
a_str = ""
b_str = ""
comma_found = False
for char in input_str:
    if char == ',':
        comma_found = True
        continue
    if not comma_found:
        a_str += char
    else:
        if char.isdigit():
            b_str += char
a = int(a_str)
b = int(b_str)
print(a % b)