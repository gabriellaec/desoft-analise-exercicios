def classifica_trinagulo(a,b,c):
    if a==b and b==c:
        return 'equilatero'
    elif a!=b and a!=c and b!=c:
        return 'escaleno'
    else:
        return 'isoceles'
print(trinagulo(3,4,5))

