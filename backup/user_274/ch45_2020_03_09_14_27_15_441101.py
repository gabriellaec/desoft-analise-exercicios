num=1
list=[]

while num > 0:
    num=int(input("Digite um número"))
    if num > 0:
    	list.append(num)
        
print(list[::-1])