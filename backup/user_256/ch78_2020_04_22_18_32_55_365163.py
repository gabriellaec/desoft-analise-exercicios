nome = input("digite o nome: ")
while nome != 'sair':
    aceleração = float(input("Digite a aceleração: "))
   
    atletas_para_tempodeprova = {}
    tempo = (200/aceleração)**0.5 
    atletas_para_tempodeprova[nome] = tempo
        
    nome = input("digite o nome: ")

print ('O vencedor é {0} com tempo de conclusão de {1} s'.format(nome, tempo))
