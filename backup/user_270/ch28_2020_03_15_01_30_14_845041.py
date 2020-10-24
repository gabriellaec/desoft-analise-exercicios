a1 = 1
an = 1/2
while an != 1/(2**100):
    a1 = a1 + an
    an = an*1/2
print(a1)
    