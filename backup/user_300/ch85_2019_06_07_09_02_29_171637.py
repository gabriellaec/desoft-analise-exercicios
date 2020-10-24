with open("macacos-me-mordam.txt", "r") as arq1:
    cont1 = arq1.read()
word ="BANANA"  
a = cont1.split(" ") 
count = 0
for i in range(0, len(a)):
	if (word == a[i]): 
		count = count + 1
             
print(count)       
  


