def eh_primo(num):
    if num<0:
        return False
    elif num == 0 or num == 1:
        return False
    else:
        if num == 2:
            return True
        elif num%2 == 0:
            return False
        else:
            x = 3
            while(x < num):
                if num % x == 0:
                    break
                x = x + 2
            if x == num:
                return True
            else:
                return False
def verifica_primos(lista):
    j=0
    dicionario={}
    while j < len(lista):
        verifica=eh_primo(lista[j])
        dicionario[lista[j]]=verifica
        j+=1
    print(dicionario)