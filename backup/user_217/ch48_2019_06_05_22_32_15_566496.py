pergunta = input("Qual é o mês escolhido: ")
lista=["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]

contador=0
while contador < len(lista):
    
    if lista[contador] == pergunta:
        print (contador + 1 )
    contador +=1
    