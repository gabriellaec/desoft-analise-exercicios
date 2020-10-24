with open('palavras.txt','r') as plvs:
    data = plvs.read()

i=0
c=[]
a=["A","a"]
es=[" ","", ","]
while i<len(data):
    if data[i] in a and data[i-1] in es:
        c.append (data[i])
    i+=1
    
print (len(c))