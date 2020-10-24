def snell_descartes(n1, n2, teta1, teta2):
    math.sin(teta2) = (n1/ n2)* math.sin(teta1)
    return teta2
a = 1
b = 2
c = 30
r = snell_descartes(a, b, c)
print(r)