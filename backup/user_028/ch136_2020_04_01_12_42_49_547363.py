import random
dado1=random.randint(1,6)
dado2=random.randint(1,6)
dado3=random.randint(1,6)
soma=dado1 + dado2 + dado3
dinheiro = 10
while dinheiro>0:
    print(dinheiro)
    dica=input('Você quer uma dica?')
    if dica == 'sim':
        dinheiro = dinheiro - 1
        chute1=int(input('Diga 1 número:')
        chute2=int(input('Diga mais 1 número:')
        chute3=int(input('Diga outro número:')
        if soma==chute1 or soma==chute2 or soma==chute3:
            print('Está entre os 3')
        else:
            print('Não está entre os 3')
    elif dica == 'não':
        print(dinheiro)
        if dinheiro<0:
            print('Perdeu')
        while dinheiro>0:
            tentativa=int(input('Chuta um número'))
            if tentativa == soma:
                print('Você ganhou!)
                dinheiro=dinheiro*5
            else:
                print('Tente novamente')
        
            