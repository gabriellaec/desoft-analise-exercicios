def simplifica_dict(dic):
    dic_list = dic.items()
    if not dic.keys() == dic.values():
        return dic_list
    
    else:
        return dic.keys()