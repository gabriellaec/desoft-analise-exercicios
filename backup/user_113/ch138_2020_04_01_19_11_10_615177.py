perg= input ("Código está executado? sim (s) ou não (n)")

if perg==n:
    print("Corrija o código e tente de novo")
    return perg
elif perg==s:
    print("O código produz o resultado correto? Sim (s) ou Não (n)")
    if n:
        print("Corrija o código e tente de novo e volte ao começo")
        return perg
    elif s:
        print("Parabens!")