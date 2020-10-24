def mais_populoso (dic):
    dic3={}
    for estado,dic2 in dic.items():
        e=0
        for habit in dic2.values():
            e+=habit
        dic3[estado]=e
    maior=0
    mest=''
    for estado,habit in dic3.items():
        if habit>maior:
            maior=habit
            mest=estado
    return mest