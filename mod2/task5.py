s = input().strip()
domains = []
current = []
for char in s:
    if char == '.':
        domains.append(''.join(current))
        current = []
    else:
        current.append(char)
domains.append(''.join(current))
for d in reversed(domains):
    print(d)