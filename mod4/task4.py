def make_palindrome(s):
    from collections import defaultdict
    count = defaultdict(int)
    for char in s:
        count[char] += 1

    odd_char = ''
    half = []
    for char, cnt in count.items():
        if cnt % 2 != 0:
            if odd_char:
                return "Нельзя составить палиндром"
            odd_char = char
        half.extend([char] * (cnt // 2))

    return ''.join(half + [odd_char] + half[::-1])


s = input().strip()
print(make_palindrome(s))