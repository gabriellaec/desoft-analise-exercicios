
def Equacao1grau (a,b):
    x = (-b)/a
    return x

v1 = int(input("Insira um valor para a: "))
v2 = int(input("Insira um valor para b: "))

resolucao = Equacao1grau(v1,v2)
print (resolucao)