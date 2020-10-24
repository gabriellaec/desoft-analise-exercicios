distancia = int(input('Qual a distancia percorrida em Km?:'))   
if distancia <200:
    def preço(distancia):
        total =(distancia * 0.5)
        return total
    print('O preço da passagem é R$ {0:.2f}'.format(preço(distancia)))
else:
    def preco(distancia):
        final = (distancia * 0.5) + (distancia - 200) * 0.45
        return final
    print('O preço da passagem é R$ {0:.2f}'.format(preco(distancia)))  
