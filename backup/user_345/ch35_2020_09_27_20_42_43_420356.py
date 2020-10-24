num=int(input('Digite um numero: '))
soma=[]
def soma_elementos(s):
    soma = s
    s = 0
    for i in range(len(soma)):
        s += l[i]
    return s


while num!=0:
    soma.append(num)
    num=int(input('Digite um numero: '))
    soma.append(num)


soma = soma_elementos(soma)
print (soma)


