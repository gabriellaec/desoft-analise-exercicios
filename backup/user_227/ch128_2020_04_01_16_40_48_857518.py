primeira_pergunta=input("O objeto está se movendo? (n/s) ")

if primeira_pergunta=="s":
    segunda_pergunta1=input("Ele deveria se mover? (n/s) ")
    if segunda_pergunta1=="s":
        print("Sem problemas!")
    
    elif segunda_pergunta1=="n":
        print("Silver tape")

elif primeira_pergunta=="n":
    segunda_pergunta2=input("Ele deveria estar parado? (n/s) ")
    if segunda_pergunta2=="s":
        print("Sem problemas!")
    
    elif segunda_pergunta2=="n":
        print("WD-40")