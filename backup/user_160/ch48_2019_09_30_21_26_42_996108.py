a = input("Qual o nome do mês?")
mes = [1,2,3,4,5,6,7,8,9,10,11,12]
i = 0
while i < len(mes):
    if a == janeiro:
        return mes[i]
    elif a == fevereiro:
        return mes[i+1]
    elif a == marco:
        return mes[a+2]
    elif a == abril:
        return mes[a+3]
    elif a == maio:
        return mes[a+4]
    elif a == junho:
        return mes[a+5]
    elif a == julho:
        return mes [a+6]
    elif a == agosto:
        return mes [a+7]
    elif a == setembro:
        return mes [a+8]
    elif a == outubro:
        return mes [a+9]
    elif a == novembro:
        return mes [a+10]
    elif a == dezembro:
        return mes [a+11]