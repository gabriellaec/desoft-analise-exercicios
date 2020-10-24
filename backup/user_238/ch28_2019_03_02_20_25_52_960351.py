def carro(v):
    if v > 80:
        resultado = 'voce foi multado no valor de ' + str((v-80)*5)
    else:
        resultado = 'voce nao foi multado'
    return resultado
b = int(input('qual a velocidade do seu carro? '))

print (carro(b))