d = 100
while d > 0:
    print("dinheiro disponivel: "+ d)
    aposta = int(input("quanto vc aposta: ")) 
    if aposta == 0:
        break 
    elif aposta > d:
        print("vc nao tem dinheiro sufucciente para a aposta")
    else:
        Tipo = input("tipo de aposta")
        if Tipo == "n" :
            numero = int(input("numero de 1 a 36: "))
            p = random.randint(1,36)
            if p == numero:
                d = d+aposta*35
            else:
                d = d-aposta
        if Tipo == "p" :
            paridade = (input("par ou impar: "))
            p = random.randint(1,2)
            if p == 1:
                p = "p"
            else:
                p = "i"
                if p == paridade:
                    d = d+aposta
                else:
                    d = d-aposta