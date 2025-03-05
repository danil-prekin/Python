phone = input().strip()
allowed = {'+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
clean = []
for char in phone:
    if char in allowed:
        clean.append(char)
print(''.join(clean))