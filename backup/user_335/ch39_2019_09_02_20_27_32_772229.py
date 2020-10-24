def somar():
    x = int(input("Digite um número: "))
    valorAcumulado = 0
    while x!=0:
        resultado = valorAcumulado+x
        valorAcumulado = resultado
        x = int(input("Digite um número: "))
    return resultado
        
print (somar())