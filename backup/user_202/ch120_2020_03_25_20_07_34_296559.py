import random
d = 100
while d > 0:
    print(f"dinheiro disponivel: {d}")
    aposta = int(input("quanto vc aposta: ")) 
    p = random.randint(0,36)
    if aposta == 0:
        break 
    elif aposta > d:
        print("vc nao tem dinheiro sufucciente para a aposta")
    else:
        Tipo = input("tipo de aposta(n - numero, p - paridade): ")
        if Tipo == "n" :
            numero = int(input("numero de 1 a 36: "))
            #print("valor do numero: {0}".format(p))
            if p == numero:
                d = d+aposta*35
            else:
                d = d-aposta
        if Tipo == "p" :
            paridade = (input("par ou impar: "))
            if p%2 == 0:
                p = "p"
            else:
                p = "i"
            if p == paridade:
                d = d+aposta
            else:
                d = d-aposta
