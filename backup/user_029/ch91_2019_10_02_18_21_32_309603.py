with open('palavras.txt','r') as palavras:
     conteudo = palavras.read()
     novo =  conteudo.split(" ")
     contador = 0
     lista = []
     lista.append(novo)
     for i in range(len(lista)):
         if i[0]== 'a' or 'A':
             contador +=1
print(contador)
palavras.close()        