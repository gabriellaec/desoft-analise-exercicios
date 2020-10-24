def inverte_dicionario(d):
    dic={}
for i in d:
if d[i] not in dic:
dic[d[i]]=[]
for i in d:
     dic[d[i]].append(i)
    return dic
