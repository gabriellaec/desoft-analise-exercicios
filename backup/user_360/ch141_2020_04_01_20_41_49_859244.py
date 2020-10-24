import random
dinheiros=1000
while dinheiros>0:
    quer=input("Você quer apostar?")
    d1=[1, 2, 3, 4, 5, 6]
    d2=[1, 2, 3, 4, 5, 6]
    if quer==sim:
        dados=random.choice(d1)
        dados2=random.choice(d1)
        dados3=dados+dados2
        chute=int(input("Qual o valor da soma dos dados?"))
        if chute==dados3:
            dinheiros=+20
        else:
            quer2=input("Quer continuar apostando ou vai desistir?")
            if quer2=='desistir':
                break
            else:
                
                
    else:
        break
                
    
