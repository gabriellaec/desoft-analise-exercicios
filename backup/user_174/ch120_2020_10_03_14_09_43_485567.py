def random.randint(saldo):
    saldo=100
    while saldo!=0:
        print("Voce tem"+ str(saldo))
        aposta("Que valor deseja apostar?")
        paridade=input("Qual a paridade do numero a ser sorteado?[p/i/n(numero exato)]")
        n="n"
        p="p"
        i="i"
        if paridade==n:
            numero=input("Digite um numero de 1 a 36:")
            numero_sorteado=radom.randit(1,36)
            