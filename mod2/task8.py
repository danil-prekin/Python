input_str = input().strip()
words = []
current_word = []
for char in input_str:
    if char == ' ':
        if current_word:
            words.append(''.join(current_word))
            current_word = []
    else:
        current_word.append(char)
if current_word:
    words.append(''.join(current_word))
result = ''.join([word[-1] for word in words])
print(result)