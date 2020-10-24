total = 0
with open ('churras.txt','r', encoding="utf8") as text_file:
    conteudos=text_file.readlines()
for i in conteudos:
    lista = str(i).split(",")
    total += float(lista[1])*float(lista[2])
print(total)