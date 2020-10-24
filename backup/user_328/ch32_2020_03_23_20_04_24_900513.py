def eh_primos(a):
    if x==1 or x==0:
        return False
    if x==2:
        return True
    if x%2==0:
        return False
    a=3
    while x>a:
        if x%a==0:
            return False
        a= a=1
        
def lista_primos(quantidade):
    contador = 1
    numero = 1
    lista = []
    while contador <= quantidade:
        if eh_primos(numero):
            lista.append(numero)
            contador += 1
        numero += 1
    return lista
lista_primos(10)

    