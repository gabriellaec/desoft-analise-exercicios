def troca(txt):
    with open(txt, 'r'):
        cont = txt.read()
        cont.replace(',', '	')
        return cont

print(troca(dados.csv))