def verifica_primos(lista):
    dic={}
    for a in lista:
        if and a != -1 and a%2 != 0 and a%3 != 0 and a%5 != 0 and a%7 != 0 or a == 7 or a == 2 or a == 3 or a == 5 or a == 1:
            dic[a]='Prime'
        else:
            dic[a]='Not Prime'
    return dic