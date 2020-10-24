n=int(input('Qual o numero?  '))
def verifica_quadrado_perfeito(n):
    x=1
    while n>0:
        n-=x
        x+=2
        return n
if n==0:
    print('True')
elif n<0:
    print('False')