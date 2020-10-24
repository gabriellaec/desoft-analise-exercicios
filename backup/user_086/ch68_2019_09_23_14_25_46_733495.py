def separa_trios(listaalunos):
    i=0
    trio=[]
    if len(listaalunos)>=3:
        while i<len(listaalunos):
            trio.append(listaalunos[i:i+3])
            i+=3
    trio.append(listaalunos[i: ])
    return trio