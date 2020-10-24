def pos_arroba(a):
    posição = 0
    for i in a:
        while i != "@":
            posição += 1
    return posição - 1
e = str(input())
print(pos_arroba(e))