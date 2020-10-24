d = int(input("dias?"))
h = int(input("horas?"))
m = int(input("minutos"))
s = int(input("segundos"))
def valor(d,h,m,s):
    y= d*24*60*60 +h*60*60 +m*60 + s
    return y
print(valor)
        