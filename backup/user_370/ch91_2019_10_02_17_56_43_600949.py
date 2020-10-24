texto=open('palavra.txt','r')
saida=open('cripto.txt','w')
for linha in texto.readlines():
    for letra in linha:
        if letra in 'Aa':
            print(letra)
        else:
            saida.write(letra)
         
texto.close()
saida.close()

