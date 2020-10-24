nome = input("digite o nome: ")
atletas_para_tempodeprova = {}
while nome != 'sair':
    aceleracao = float(input("Digite a aceleração: "))
    tempo = (200/aceleracao)**0.5 
    atletas_para_tempodeprova[nome] = tempo
        
    nome = input("digite o nome: ")

print ('O vencedor é {0} com tempo de conclusão de {1} s'.format(nome, tempo))
