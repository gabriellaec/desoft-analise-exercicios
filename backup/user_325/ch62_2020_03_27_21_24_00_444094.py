def por_arroba(s):
    i = 0
    while i < len(s):
        if "@" in s:
            print(s[i])
        i +=1
    return s