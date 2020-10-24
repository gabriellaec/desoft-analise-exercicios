lista_num = []
rodando = True
while rodando:
    numero = int(input("digite um numero: "))
    if numero > 0:
        lista_num.append(numero)
    if numero <= 0:
        rodando = False
        
print(lista_num[::-1])