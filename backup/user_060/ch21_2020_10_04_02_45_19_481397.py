d = input("dias?\n")
h = input("horas?\n")
m = input("minutos?\n")
s = input("segundos?\n")
def valor(d,h,m,s):
    valor = d*24*60*60 + h*60*60 + m*60 + s
    return valor
print(valor)
    