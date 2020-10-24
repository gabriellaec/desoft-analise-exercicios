secondList = []
def inverte_lista(firstList):
    counter = len(firstList)-1
    while counter >= 0:
        secondList.append(firstList[counter])
        counter-=1
    return secondList
