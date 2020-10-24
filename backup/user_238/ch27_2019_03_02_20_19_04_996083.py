def reducao(cigarros,anos):
        vida=cigarros*365*cigarros*(1/144)
        return vida
anos=int(input('ha quantos anos voce fuma? '))
cigarros=int(input('quantos cigarros voce fuma por dia? '))

resposta=reducao(cigarros,anos)
print(resposta)
