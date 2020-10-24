x=int(input('Sua idade: '))
def testa_maioridade(idade):
    if idade >= 18:
        return 'Adulto'
    elif idade >=12:
        return "Adolescente" 
    else:
        return "crianca"

print(testa_maioridade(x))
