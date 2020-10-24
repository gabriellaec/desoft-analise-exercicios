with open('dados.csv', "r") as file:
    x=file.read()
y=x.replace(',' , '\t')
print(y)
    