def eh_primo(num):
    if num == 0 or num == 1:
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
def maior_primo_menor_que(n):
    confere=eh_primo(n)
    i=0
    lista=[]
    while i<=n:
        if eh_primo(i)==True:
            lista.append(i)
            i+=1
        elif eh_primo(i)==False:
            i+=1
    print (max(lista))

    if lista==[]:
            print (-1)

       