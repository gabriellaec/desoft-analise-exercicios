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
    count2 = 1 #listafatorial
    count3 = 0 #while
    conta = 1 + x
    conta2 = conta
    while count3<=n:
        conta2 += (x**count)/(listafatorial[count2])
        counnt +=1
        count2 +=1
        count3 +=1
    return conta2