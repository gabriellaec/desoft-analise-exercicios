numero= int(input("Digite um numero"))
dic={1:"Janeiro", 2:"Fevereiro", 3:"Março", 4:"Abril", 5:"Maio", 6:"Junho", 7:"Julho", 8:"Agosto", 9:"Setembro", 10:"Outubro", 11:"Novembro", 12:"Dezembro"} 
print(dic[numero])

listanum=[1,2,3,4,5,6,7,8,9,10,11,12]
listanom=["Jan","Fev","Abr","Mar","Maio","Jun","Jul", "Ago","Set","Out","Nov","Dez"]
for i in listanum:
    if i==numero:
        print(listanom[i])