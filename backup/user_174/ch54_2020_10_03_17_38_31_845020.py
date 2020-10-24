def calcula_fibonacci():
    n=input("Digite o numero de elementos da sequencia que voce quer: ")
    F1=1
    F2=1
    lista=[F1,F2]
    i=0
    while i<=int(n)-3:
        F1=lista[i]+list[i+1]
        lista.append(F1)
        i=i+1
        return lista
    calcula_fibonacci()
        