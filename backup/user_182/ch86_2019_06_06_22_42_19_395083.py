
with open("dados.csv", "r", encoding="utf*") as arquivo:
    conteudo = arquivo.read()
    
novoconteudo=conteudo.replace(",", "\t")

print(novoconteudo)

with open("arquivotab.tab", "w") as arquivo:
    arquivo.write(novoconteudo)
    