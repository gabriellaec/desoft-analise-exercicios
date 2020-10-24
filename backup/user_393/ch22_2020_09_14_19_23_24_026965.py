def tempo_de_vida_perdido_em_dias(x,z):
    y = (x*(10/1440))*z*365
    return y

num1= int(input("quantos cigarros você fuma por dia?"))
num2= int(input("há quantos anos você fuma?"))
a = tempo_de_vida_perdido_em_dias(num1,num2)
print(a)


