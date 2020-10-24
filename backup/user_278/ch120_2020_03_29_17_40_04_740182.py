import random
roleta= random.randint(0,36)
dinheiro= 100   #sempre mostrar o dinheiro disponível  
dinheiro_suficiente=True
aposta_nao_eh_zero=True
continuar=True

def eh_par(roleta):
    if roleta%2==0:
        return True

print ("Dinheiro inicial: {} ".format(dinheiro))
while dinheiro > 0 and dinheiro_suficiente and aposta_nao_eh_zero and continuar: 
    dinheiro_suficiente=True
    continuar= input("Deseja apostar? s/n: ")
    if continuar=="s":
        continuar=True
        aposta= int(input("Que valor deseja apostar?: "))
        if aposta!=0:
            aposta_nao_eh_zero=True
            qual_aposta= input("A aposta é número ou paridade? n/p: ")
            if qual_aposta=="n":
                digite= input("Digite um valor entre 0 e 36: ")
                if digite==roleta:
                    dinheiro= dinheiro + aposta * 35
                    print ("Acertou! Dinheiro disponível= {0}".format(dinheiro))
                else:
                    dinheiro = dinheiro - aposta
                    print ("Errou. Dinheiro disponível= {0}".format(dinheiro))
            elif qual_aposta=="p":
                par_ou_impar= input("Par ou ímpar? p/i: ")
                if par_ou_impar=="p":
                    if eh_par(roleta)==True:
                        dinheiro = dinheiro + aposta
                        print ("Acertou! Dinheiro disponível= {0}".format(dinheiro))
                    else:
                        dinheiro = dinheiro - aposta
                        print ("Errou. Dinheiro disponível= {0}".format(dinheiro))
                elif par_ou_impar=="i":
                    if eh_par(roleta)==False:
                        dinheiro = dinheiro + aposta
                        print ("Acertou! Dinheiro disponível= {0}".format(dinheiro))
                    else:
                        dinheiro = dinheiro - aposta
                        print ("Errou. Dinheiro disponível= {0}".format(dinheiro))   
        else:
            aposta_nao_eh_zero=False
    else:
        continuar=False 
print ("Acabou o jogo, volte sempre")   