#Funçao que recebe um inteiro positivo n e retorna uma string contendo uma sequencia n de asteriscos

def recebe_inteiro (n):
    aster = '*' * n
    return aster

num = int(input('Digite um numero:'))
print (recebe_inteiro(num))
