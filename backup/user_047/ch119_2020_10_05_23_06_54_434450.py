def calcula_euler(x,n):
    contador = 1
    resultado = 1
    listafatorial=[]
    while contador!=n:
        conta = contador*resultado
        listafatorial.append(resultado)
        resultado +=conta
        contador +=1
    count = 2 #x^2
    c = 1 #listafatorial
    count3 = 0 #while
    conta = 1 + x
    conta2 = conta
    while count3!=n-2:
        conta2 += (x**count)/(listafatorial[c])
        count +=1
        c +=1
        count3 +=1
        print (conta2, count3 )
    return conta2
a = calcula_euler(10,20)
print(a)
