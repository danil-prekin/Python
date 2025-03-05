s, i = input().split(',')
i = i.strip()
s = s.strip()
count = 0
for char in s:
    if char == i:
        count += 1
    else:
        break
print(count)