c = input ("Qual o mês?")
a = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
b = [1,2,3,4,5,6,7,8,9,10,11,12]
i=0
while c != a[i]:
    i+=1
if a[i] == c :
    print(b[i])