def classifica_idade(idade):
    idade=int(input('Escreva um numero inteiro maior que 0: '))
    if idade<11 or idade==11:
        print('crianca')
    elif idade>11 and idade<18:
        print('adolescente')
    else:
        print('adulto')
    return idade
print(classifica_idade(idade))
 

    