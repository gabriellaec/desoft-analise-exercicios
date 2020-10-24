import csv
def custo_churras(list0):
    total=[]
    for paragraph in list0:
        valor = (float(paragraph[1]))*(float(paragraph[2]))
        total.append(valor)
    print(total)
    return sum(total)
        
            


return_list=[]
with open ("churras.txt" , "r", encoding="utf8") as file1:

    reader = csv.reader(file1)
    return_list = list(reader)
    
print(custo_churras(return_list))
