d = input("dias?")
h = input("horas?")
m = input("minutos?")
s = input("segundos?")
def valor(d,h,m,s):
    valor = d*24*60*60 + h*60*60 + m*60 + s
    return valor
print(valor)
    