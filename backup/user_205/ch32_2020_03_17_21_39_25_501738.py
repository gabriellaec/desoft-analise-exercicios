def lista_primos(numero):
    lista = [2, ] 
    primo = 3
    while numero > primo:
        primo+=2
        if (numero % primo == 0):
            break
        else:
            lista.append (primo)