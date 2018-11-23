
players2 =[['1','asso1','name1'],['2','asso1','name2'],['3','asso1','name3'],['4','asso1','name4'],['5','asso1','name5'],['6','asso2','name6'],['7','asso2','name7'],['8','asso2','name8'],['9','asso2','name9'],['10','asso2','name10']]
players3 =[['1','asso1','name1'],['2','asso1','name2'],['3','asso1','name3'],['4','asso1','name4'],['5','asso1','name5'],['6','asso2','name6'],['7','asso2','name7'],['8','asso2','name8'],['9','asso2','name9'],['11','asso2','name11'],['12','asso2','name12']]
players4 =[['1','asso1','name1'],['2','asso1','name2'],['3','asso1','name3'],['4','asso1','name4'],['5','asso1','name5'],['6','asso2','name6'],['7','asso2','name7'],['8','asso2','name8'],['9','asso2','name9'],['11','asso2','name11'],['12','asso2','name12'],['13','asso2','name13']]


players1 =[['1','asso1','name1'],['2','asso1','name2'],['3','asso1','name3'],['4','asso1','name4'],['5','asso1','name5'],['6','asso2','name6'],['7','asso2','name7'],['8','asso2','name8'],['9','asso2','name9']]


d = dict()
for player in players4:
    if player[1] in d:
        d[player[1]].append([player[0],player[2]])
    else:
        d.setdefault(player[1],[])
        d[player[1]].append([player[0],player[2]])

newList =[]
while (d!={}):
    for asso in d.keys(): 
        newList.append(d[asso][0])
        d[asso].remove(d[asso][0])
        if(d[asso]==[]):
            del d[asso]
        if(d=={}):
            break

print newList