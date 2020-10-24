def imprime_tipo(n):
    if (n%3) == 0 and (n%5) != 0:
        print("Tipo A")
    if (n%5) == 0 and (n%3) != 0:
              print ("Tipo B")
    if (n%3) == 0 and (n%5) == 0:
                         print("Tipo C")
    if (n%3) != 0 and (n%5) != 0:
                         print ("Tipo D")
                         
    