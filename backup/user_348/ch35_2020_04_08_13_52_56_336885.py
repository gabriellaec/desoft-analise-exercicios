número = True 
soma = 0
while número:
    resposta = float(input('digite um numero:'))
    if resposta != 0:
        soma = soma + resposta
        número = True 
    else:
        número = False
        print(soma)