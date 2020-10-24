print("vamos descobrir se um triângulo é equilátero,isósceles ou escaleno")
a= int(input("insira o primeiro lado: "))
b= int(input("insira o segundo lado: "))
c= int(input("insira o terceiro lado: "))
if a== b ==c:
    print("é equilátero")
elif a==b or a==c or b==c:
    print("é isósceles")
else:
    print("é escaleno")