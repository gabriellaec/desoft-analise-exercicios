km = int(input())
def preco_passagem(km):
    if km <= 200:
        preco = (km*0.5)
    else:
        preco = (200*0.5) + km*0.45
    print(preco)