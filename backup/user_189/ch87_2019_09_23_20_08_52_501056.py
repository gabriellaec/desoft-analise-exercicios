import csv
def custo_churras(list0):
    total=[]
    i=0
    for paragraph in list0:
        while i<len(paragraph):
            valor = (float(paragraph[1]))*(float(paragraph[2]))
            total.append(valor)
            i+=1
    return sum(total)
        
            


return_list=[]
with open ("churras.txt" , "r", encoding="utf8") as file1:

    reader = csv.reader(file1)
    return_list = list(reader)
    
print(custo_churras(return_list))
