
palavra = "O rato roeu"
palavra.lower()
"o rato roeu"
palavra.upper()
"O RATO ROEU"
print (palavra.startswith ("O"))
print (palavra.upper().startswith("ratinho"))
print (palavra.find("e"))
print (palavra.lower().endswith("roeu"))
def f(x):
    y = 6*x + 3
    return y 
print (f(3))
print (f(0))

começo = int(input("Olá caro padawan! Para respostas sim digita numeros maior que 10. Para não faça o contrário: "))
Inteligencia = int(input("Olá chefe! Quer saber como será o dia de hoje: "))
if Inteligencia > 10:
    print ("Hoje é dia 27 de março! Tempo parcialmente nublado com tempo frio!")
    print ("Meus algoritmos indicam baixa umidade e tempo seco")
    print ("Como essa cidade é poluída em! Ainda bem que sou só um robô")
    print ("De qualquer forma, estou aqui para auxiliá-lo! e lhe dar conselhos valiosos")
    print ("Enfim, ")
    casaco = int(input("Acho melhor levar um casaco! Quer um:  "))
    if casaco > 10:
        print ("Ok! Vai estar na porta para você! Aliás, seu cafezinho também esta sendo feito")
    else:
        print ("Tudo bem, se ficar doente só falar comigo kkkkkkkk")
    felicidade = int(input("Você se sente feliz com essa I.A: "))
    if felicidade > 10:
        print ("Que bom! Também gosto de você")
    else:
        print("Affe, então sai daq q tem outros q me querem, bjos")
else:
    print ("Parece que o senhor não vai trabalhar né")
    trabalho = int(input("Quer assistir netflix ou não: "))
    if trabalho > 10:
        print ("Opa! Ai sim! A série eu escolho pq sou autoritária mesmo, vai ser TERRA PLANA kkkkk")
    else:
        print ("Então durma! Descansar nunca é demais.")

    

