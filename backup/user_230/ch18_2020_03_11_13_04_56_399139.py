a=int(input("Quantos anos voce tem?"))
if a>=21:
    print("Liberado EUA e BRASIL")
elif a>=18 and a<21:
    print("Liberado BRASIL")
else:
    print("Não está liberado")
