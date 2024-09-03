def compress(s):
    result = ''
    prev_char = ''
    for char in s:
        if char == prev_char:
            result += '*'
        else:
            result += char
        prev_char = char
    return result
s='balloon'
print(compress(s))