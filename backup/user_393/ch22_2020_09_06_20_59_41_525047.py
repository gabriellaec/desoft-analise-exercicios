 def f(x,z):
    y= -(x*(10/1440))*z*365
    return y

num1= int(input("quantos cigarros você fuma por dia?"))
num2= int(input("a quantos anos você fuma?"))
a= f(num1,num2)
print(a)


