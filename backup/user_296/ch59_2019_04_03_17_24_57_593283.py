def conta_a(b):
    i = 0
    for m in b:
        if m == "a":
            i += 1
    return i
palavra = str(input())
print(conta_a(palavra))
    