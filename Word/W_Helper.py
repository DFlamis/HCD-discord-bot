import Saki_Helper as skh

#Dictionary
DFlamis = {'home':{'clipboard':['copiar','pegar','copiar formato','cortar'],'font':['negrita','cursiva','subrayado'],'paragraph':[]},
            'insert':[],
            'draw':[],
            'design':[],
            'layout':[],
            'references':[],
            'mailings':[],
            'reviews':[]}

def match(message):
    #Remove useless characters
    list_TM = message.split(' ')

    set_m = set(list_TM)
    variable = 0
    orasion = ''
    
    for n in DFlamis:
        for m in DFlamis[n]:
            set_d = set(DFlamis[n][m])

            if skh.is_bigger(variable,len(set_m & set_d)):
                variable = len(set_m & set_d)

                orasion = skh.sentence_starter()+' ' + n + ' ' + skh.second() + ' ' + m

    return orasion
