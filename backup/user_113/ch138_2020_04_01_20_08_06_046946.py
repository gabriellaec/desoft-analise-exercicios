print ("Código está executando? Sim (s) ou Não (n)")
resp= input ("s, n")
if resp== input("n"):
    print("Corrija o código e tente de novo")
    
elif resp== input("s"):
    print("O código produz o resultado correto? Sim (s) ou Não (n)")
    if resp== input("n"):
        print("Corrija o código e tente novamente")
       
    elif resp==input("s"):
        print("Parabens!")