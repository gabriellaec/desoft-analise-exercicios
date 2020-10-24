def imprime_tipo(n):
    if n%3==0 and n%5!=0:
        print ("Tipo A")
    elif n%3!=0 and n%5==0:
        print ("Tipo B")
    elif n%3==0 and n%5==0:
        print ("Tipo C")
    elif n%3!=0 and n%5!=0:
        print ("Tipo D")