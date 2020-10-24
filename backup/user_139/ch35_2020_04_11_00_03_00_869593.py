soma = 0
pergunta = True
while pergunta:
    resp = int (input ('Digite um número: ')
    if resp == 0:
        pergunta = False
        print (soma)
    else:
        soma = soma + resp