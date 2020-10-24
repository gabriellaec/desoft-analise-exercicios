
def preco_passagem(km):
    km = int(input())
    if km <= 200:
        preco = (km*0.5)
    if km > 200:
        preco = (200*0.5) + km*0.45
    print(preco)