pergunta = True
soma = 0
while pergunta:
    resp = input ('Digite um número: ')
    if resp == 0:
        print (soma)
        pertunta = False
    else:
        soma = soma + resp