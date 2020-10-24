velocidade = int(input())
if velocidade > 80:
    print("Você foi multado")
    print(float((velocidade-80)*5),"%.2f")