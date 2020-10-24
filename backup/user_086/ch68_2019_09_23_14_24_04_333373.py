def separa_trios(listaalunos):
    i=0
    trio=[]
    while i<len(listaalunos) and i+3<=len(listaalunos):
        trio.append(listaalunos[i:i+3])
        i+=3
    trio.append(listaalunos[i: ])
    return trio