# def stock_list(stocklist, categories):
#     # your code here
#     if stocklist == []:
#         return ''
#     dico = {}
#     for cat in categories:
#         dico[cat] = 0
#     for stock in stocklist:
#         spi = stock.split(',')
#         spliter = spi[0].split(' ')
#         if spliter[0][0] in dico:
#             dico[spliter[0][0]] += int(spliter[1])

#     string = ''
#     for k, v in dico.items():
#         string += f"({k} : {v}) - "
#     return string[:-3]

######################################################

def parse(data):
    liste=[]
    r=0
    for i in data:
        if i == "i":
            r+=1
        if i == "s":
            r=r**2
        if i == "o":
            liste += [r]
        if i == "d":
            r-=1
            
    return liste

print(parse("iiisdoso"))

########################################################

def find_missing(sequence):
    
    differences = []
    for k in range(1,len(sequence)):
        differences.append(sequence[k]-sequence[k-1])
        
    if differences[0] < 0:
        minimum = max(differences)
        maximum = min(differences)
    else:
        minimum = min(differences)
        maximum = max(differences)
    index = differences.index(maximum)
    
    return sequence[index]+minimum

print(find_missing([1, 3, 5, 9, 11]))