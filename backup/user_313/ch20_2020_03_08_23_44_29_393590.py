a = int(input('Qual distancia voce deseja percorrer: '))

if ( a <= 200):
    print(round((a * 0.50),2))

if ( a > 200):
    print(round(((a*0.50))+((0.45*a-200)),2))