def programa():
    print ("Código está executando? Sim (s) ou Não (n)")
    resp= input ("s, n")
    if resp== input("n"):
        print("Corrija o código e tente de novo")
        return programa
    elif resp== input("s"):
        print("O código produz o resultado correto? Sim (s) ou Não (n)")
        return programa
        if resp== input("n"):
            print("Corrija o código e tente novamente")
            return programa
        elif resp==input("s"):
            print("Parabens!")
            return programa