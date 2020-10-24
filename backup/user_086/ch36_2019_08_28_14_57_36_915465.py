numero=int(input('Digite um número para verificar se ele é primo: '))
def eh_primo(numero):
    impar=3
    if numero==2:
        return True
    if numero%2==0:
        return False
    while impar<numero:
        if numero%impar==0:
            return False
        impar+=2
    return True
print(eh_primo(numero))