def simplifica_dict(dic):
    
    output=[]
    for key in dic.keys():
        output.append(key)

    return output

dic={"a":1,"b":2,"c":4}
print(simplifica_dict(dic))