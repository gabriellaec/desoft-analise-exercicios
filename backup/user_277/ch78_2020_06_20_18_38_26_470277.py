def calcula_tempo (atletas):
    tempo = {}
    for nome, a in atletas.items():
        t = (200/a)**(1/2)
        tempo[nome] = t
    return tempo

i = True
while i:
    nome = input("digite um nome:")
    if nome != 'sair'
        aceleracao = int(input("digite a aceleração:"))
    else:
        i = False
 