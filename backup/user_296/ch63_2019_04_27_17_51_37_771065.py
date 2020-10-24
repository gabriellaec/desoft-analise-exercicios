def pos_arroba(x):
    i =0
    for n in x:
        if n == "@":
            return i 
        i += 1
    return i
a = str(input())
print(pos_arroba(a))
            