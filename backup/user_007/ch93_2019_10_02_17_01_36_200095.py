def give_Digits(num):
    c = 1
    ans = []
    while num >= c:
        ans.append(int((num%(c*10))/c))
        c *= 10
    return ans

def verifica_numero(num):
    if num < 1:
        return False
    lista = give_Digits(num)
    soma = 0
    for i in lista:
        soma += i**i
    if soma == num:
        return True
    else:
        return False