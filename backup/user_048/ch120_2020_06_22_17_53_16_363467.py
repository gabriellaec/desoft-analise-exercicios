import random 

continua = True
while continua:
    dinheiro=100
    if 0>=dinheiro:
        continua=False
    print(dinheiro)
    aposta=int(input('quanto apostar?'))
    if aposta==0:
        continua = False
    else:
        pass
    tipo=input('tipo da aposta(n ou p/i?)')
    if tipo == 'n':
        escolha=int(input('escolha um numero de 1 a 36'))
        sorteio=random.randint(1,36)
        if escolha == soretio:
            dinheiro+=aposta*10
        else:
            dinheiro-=aposta
    if tipo == 'p':
        escolha=int(input('escolha um numero de 1 a 36'))
        sorteio=random.randint(1,36)
        if escolha%2== 0 and soretio%2==0 :
            dinheiro+=aposta
        else:
            dinheiro-=aposta
    if tipo == 'i':
        escolha=int(input('escolha um numero de 1 a 36'))
        sorteio=random.randint(1,36)
        if escolha%2!=0 and sorteio %2!=0:
            dinheiro+=aposta
        else:
            dinheiro-=aposta
    
    