número = True 
while número:
    resposta = float(input('digite um numero:'))
    if resposta != 0:
        número = True 
    else:
        número = False
        print(resposta)