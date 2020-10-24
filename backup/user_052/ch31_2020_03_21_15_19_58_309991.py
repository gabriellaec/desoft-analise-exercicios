n = int(input("Digite um número:"))
if n < 0:
    print ("Número inválido. Digite apenas valores positivos")
if n == 0 or n == 1:
    print ("%d é um caso especial." %n)
else:
    if n == 2:
        print ("%d é um número primo." %n)
    elif n%2 == 0:
        print("%d não é primo, pois 2 é o único número par primo." %n)
    else:
        print ("É um numero ímpar")