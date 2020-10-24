def primo(num):
    primo = True
    a = 2
    while a < num:
        if num%a == 0:
            primo = False       
        a+=1
    return primo

def verifica_primos(lista):
    dic = {}
    for n in lista:
        dic[n]=primo(n)
    return dic