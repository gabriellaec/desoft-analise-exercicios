with ('dados.csv','r') open as arquivo:
    original = arquivo.read()
    dados.tsv = original('tsv')
    