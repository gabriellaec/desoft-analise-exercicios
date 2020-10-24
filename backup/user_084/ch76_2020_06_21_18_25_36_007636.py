def aniversariantes_de_setembro(DICI):
    DICI_final={}
    for c in DICI:
        if DICI[c][4]==9:
            DICI_final[c]=DICI[c]
    return DICI_final
x={'Nico Uno': '01/01/1992', 'Horácio P. Genaro': '03/03/1992', 'Ukibe Nokome': '05/05/1992', 'Maurício Melo': '07/09/1992', 'Abigail Oliveira': '09/09/1992'}
print(aniversariantes_de_setembro(x)