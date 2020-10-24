def apaga_repetidos (s):
    s = s.lower()
    print(s)
    li = []
    for i in range (len(s)):
        li.append(s[i])
    for a in range(len(li)):
        b = a + 1
        while b < len(li):
            if li[a] == li[b] and li[a] != '*':
                li[b] == '*'
            b += 1
    n = ''.join(li)
    return n