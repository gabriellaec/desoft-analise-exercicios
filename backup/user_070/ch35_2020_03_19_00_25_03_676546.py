i = True
s = 0
while i:
    n = float(input('numero: '))
    if n == 0:
        i = False
    else:
        s = s + n
print(s)