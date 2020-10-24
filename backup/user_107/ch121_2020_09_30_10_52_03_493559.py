def subtracao_de_listas (list1, list2):
    subtracted_list = []
    
    for item1 in list1:
        has_in_list2 = False
        
        for item2 in list2:
            if item1 == item2:
                has_in_list2 = True
                
        if not has_in_list2:
            subtracted_list.append(item1)

    return subtracted_list
