n=float(input("Digite um número : "))
b=2
while abs(n-(b*b))>0.00001:
    p=(b+(n/b))/2
    b=p
print ("A raiz quadrada de %d é aproximadamente %8.4f" % (n, p))