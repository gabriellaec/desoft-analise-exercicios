x=int(input("Qual a distância você deseja percorrer em km? "))
if x<200:
        print("O valor da passagem é R$ {0:.2f}".format(float(x*0.5)))
else:
        print("O valor da passagem é R$ {0:.2f}".format(float((200*0.5)+(x-200)*0.45)))
    