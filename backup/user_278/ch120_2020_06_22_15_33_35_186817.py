import random
dinheiro= 100   #sempre mostrar o dinheiro disponível  


def eh_par(roleta):
    if roleta%2==0:
        return True

while dinheiro > 0:
    print (dinheiro)
    roleta= random.randint(0,36)
    aposta= float(input("Que valor deseja apostar?: "))
    
    if aposta!=0 and aposta<=dinheiro:
        qual_aposta= input("A aposta é número ou paridade? n/p: ")
        if qual_aposta=="n":
            digite= int(input("Digite um valor entre 0 e 36: "))
            if digite==roleta:
                dinheiro+= aposta * 35
            else:
                dinheiro -= aposta
        elif qual_aposta=="p":
            par_ou_impar= input("Par ou ímpar? p/i: ")
            if par_ou_impar=="p":
                if eh_par(roleta):
                    dinheiro += aposta
                else:
                    dinheiro -= aposta
            elif par_ou_impar=="i":
                if eh_par(roleta)==False:
                    dinheiro += aposta
                else:
                    dinheiro -= aposta
    else:
        break