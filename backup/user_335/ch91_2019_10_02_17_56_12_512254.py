def contador_de_a (texto): #Função para a contagem de letras A
    numeros_de_a = 0 #Contador para armazenar a quantidade de palavras iniciadas com A
    listapalavras = texto.split() #Lista em que cada item é uma palavra
    for p in listapalavras: #loop para verificar cada item
        if p[0] == "A" or "a": #Verificando se ela se inicia com A ou a
            numeros_de_a += 1 #Se verdadeiro, adiciona +1 ao contador
    return numeros_de_a #Retornar o valor final do contador


with open ('palavras.txt', "r") as arquivo: #Abrir o arquivo e permitir a leitura dele
    TextoDoArquivo = arquivo.read() #Ler o arquivo e armazenando na variável texto
    
print (contador_de_a(TextoDoArquivo)) #Exibir no console o número de palavras iniciadas em A