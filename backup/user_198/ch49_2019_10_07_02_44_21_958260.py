par={}
num=int(input("Entre com um número par positivo: "))
while num>0:
    par.append(num)
    num=int(input("Entre com outro número par positivo: "))
par.sort(reverse=True)
