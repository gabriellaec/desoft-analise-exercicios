
from random import randint 

dinheiro=100    
print(dinheiro)        
while dinheiro>0:
    aposta=int(input("qual o valor da aposta? "))
    if aposta !=0:
        opcao=input("a aposta é em um número ou paridade? ")
        if opcao == "n":
            numero=int(input("numero de 1 a 36: "))
            roleta=randint(0,36)
            if numero == roleta:
                dinheiro+=(aposta*35)
                print(dinheiro)
            else:
                dinheiro-=aposta
                print(dinheiro)

        elif opcao == "p":
            p_ou_i=input("par ou impar? ")
            if p_ou_i == "p":
                roleta=randint(0,36)
                if roleta % 2 == 0 or roleta==0:
                    dinheiro+=aposta
                    print(dinheiro)
                else:
                    dinheiro-=aposta  
                    print(dinheiro)   
            elif p_ou_i == "i":
                roleta=randint(0,36)
                if roleta % 2 != 0 and roleta !=0:
                    dinheiro+=aposta
                    print(dinheiro)
                else:
                    dinheiro-=aposta
                    print(dinheiro)
    else:
        dinheiro-=dinheiro            
