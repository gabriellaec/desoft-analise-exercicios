def classifica_triangulo(a, b, c):
if a == b and a == c:
return 'Equilátero'
elif a != b and a != c and b != c:
return 'Escaleno'
else:
return 'Isósceles'