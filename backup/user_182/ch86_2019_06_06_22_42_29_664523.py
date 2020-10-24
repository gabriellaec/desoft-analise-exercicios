
with open("dados.csv", "r", encoding="utf*") as arquivo:
    conteudo = arquivo.read()
    
novoconteudo=conteudo.replace(",", "	")

print(novoconteudo)

with open("dados.tsv", "w") as arquivo:
    arquivo.write(novoconteudo)
    