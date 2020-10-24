palavras=[]
palavra=""
i=0
ON=True
while ON:
    palavra=input()
    if palavra=="fim":
        ON=False
    else:
    	palavras[i]=palavra
    i+=1
j=0
while j<len(palavras):
    if palavras[j][0]=="a":
    	print(palavras[j])
    j+=1

	