s = input().strip()
count_0 = 0
count_1 = 0
for char in s:
    if char == '0':
        count_0 += 1
    elif char == '1':
        count_1 += 1
print('yes' if count_0 == count_1 else 'no')