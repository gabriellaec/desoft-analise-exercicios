número = True 
while número:
    soma = 0
    resposta = float(input('digite um numero:'))
    if resposta != 0:
        soma = soma + resposta
        número = True 
    else:
        número = False
        print(soma)