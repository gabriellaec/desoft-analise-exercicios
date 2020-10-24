mes = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
q_mes = input("nome do mes")
i = 0
while i<len(mes):
    if q_mes == mes[i]:
        print i
    else:
        i+=1