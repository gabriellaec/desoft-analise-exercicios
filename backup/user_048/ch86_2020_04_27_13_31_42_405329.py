with open('dados.csv', "r") as file:
    x=file.read()
y=x.replace(',' , '\t')

with open('dados.tsv"w+") as file:
    z=file.write(y)
