def subtracao_de_listas (list1, list2):
    merged_list = []
    
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                merged_list.append(item1)

    return merged_list
