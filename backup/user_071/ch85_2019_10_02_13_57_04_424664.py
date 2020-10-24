import csv
lista=[]
with open('macacos_me_mordam', newline='') as csvfile:
    spamreader=csv.reader(csvfile, delimiter=',')
    for linha in spamreader:
        lista.append(linha)
print(lista)