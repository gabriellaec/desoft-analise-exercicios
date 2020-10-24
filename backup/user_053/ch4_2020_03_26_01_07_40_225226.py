def classifica_idade(idade):
    if idade<12:
        classificacao = 'crianca'
    elif idade>11 and idade<18:
        classificacao = 'adolescente'
    else:
        classificacao = 'adulto'
    return classificacao

print('-------------------------------------------------')

a=5

b=classifica_idade(a)
print('-------------------------------------------------')
print(b)