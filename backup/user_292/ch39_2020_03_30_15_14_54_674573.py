def tamanho(numero):
    x=1
    while numero>1:
        if numero%2==0:
            numero=numero/2
            x+=1
        else:
            numero=numero*3+1
            x+=1
    return x
numero=1
maior_tamanho=0
numero_com_maior_tamanho=0
while numero<1000:
    numero+=1
    if tamanho(numero)>maior_tamanho:
        maior_tamanho=tamanho(numero)
        numero_com_maior_tamanho=numero
print(numero_com_maior_tamanho)