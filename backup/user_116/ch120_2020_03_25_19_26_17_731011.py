from random import randint 

dinheiro=100    
print(dinheiro)        
while dinheiro>0:
    aposta=int(input("qual o valor da aposta? "))
    if aposta !=0:
        opcao=input("a aposta é em um número ou paridade? ")
        if opcao == "n":
            numero=int(input("numero de 1 a 36: "))
            roleta=randint(2,35)
            if numero == roleta:
                dinheiro+=(aposta*35)
                print(dinheiro)
            else:
                dinheiro-=aposta
                print(dinheiro)
        elif opcao == "p":
            roleta=randint(0,36)
            if roleta % 2 == 0 or roleta==0:
                dinheiro+=aposta
                print(dinheiro)
            else:
                dinheiro-=aposta  
                print(dinheiro)   
        elif opcao == "i":
            roleta=randint(0,36)
            if roleta % 2 != 0 and roleta !=0:
                dinheiro+=aposta
                print(dinheiro)
            else:
                dinheiro-=aposta
                print(dinheiro)
    else:
        dinheiro-=dinheiro            







