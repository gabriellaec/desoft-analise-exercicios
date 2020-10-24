Programa=True
x=input("Código está executando?")
if x==n:
    print("Corrija o código e tente de novo")
    Programa=True
if x==s:
    y=input("O código produz o resultado certo?")
    if y==n:
        print("Corrija o código e tente de novo e volte para o começo de tudo")
        Programa=True
    elif y==s:
        print ("Parabéns!")
        Programa=False
    