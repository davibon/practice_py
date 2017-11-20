def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
        result = result + s[i]
        i = i + 1

    return result

def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1
