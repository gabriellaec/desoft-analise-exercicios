import random
d = 100
while d > 0:
    print("dinheiro disponivel: {0}".format(d))
    aposta = int(input("quanto vc aposta: ")) 
    if aposta == 0:
        break 
    elif aposta > d:
        print("vc nao tem dinheiro sufucciente para a aposta")
    else:
        Tipo = input("tipo de aposta(n - numero, p - paridade): ")
        if Tipo == "n" :
            numero = int(input("numero de 1 a 36: "))
            p = random.randint(1,36)
            #print("valor do numero: {0}".format(p))
            if p == numero:
                d = d+aposta*35
            else:
                d = d-aposta
        if Tipo == "p" :
            paridade = (input("par ou impar: "))
            j = random.randint(1,2)
            if j == 1:
                j = "p"
            else:
                j = "i"
            #print("paridade:"+j)
            if j == paridade:
                d = d+aposta
            else:
                d = d-aposta
