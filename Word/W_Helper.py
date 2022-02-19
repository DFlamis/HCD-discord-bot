import Saki_Helper as skh

#Features BETA (It Works)
# DFlamis = {'home':{
#             'clipboard':['copiar','pegar','copiar formato','cortar'],'font':['negrita','cursiva','subrayado'],'paragraph':[]},
#             'insert':[],
#             'draw':[],
#             'design':[],
#             'layout':[],
#             'references':[],
#             'mailings':[],
#             'reviews':[]}

#Features Experimental LIST
# DFlamis = {'home':{'clipboard':{'copiar':['copiar','copio'],'pegar':['pegar','pego'],'cortar':['corto','cortar'],'copiar formato':['copio','copiar','formato']},
#                     'font':{'fuente':['tipo','letra','fuente','cambiar','cambio','letra'],'tamaño':[],'borrar formato':[],'negrita':[],'cursiva':[],'subrayado':[],'':[],'':[],'':[],'':[],'':[],'':[],'':[],'':[],},
#                     'paragraph':{}},
#             'insert':[],
#             'draw':[],
#             'design':[],
#             'layout':[],
#             'references':[],
#             'mailings':[],
#             'reviews':[]}

#Features
DFlamis = {'home':{'clipboard':{'copiar':{'copiar','copio'},
                                'pegar':{'pegar','pego'},'cortar':{'corto','cortar'},
                                'copiar formato':{'copio','copiar','formato'}},
                    'font':{'fuente':{'tipo','letra','fuente','cambiar','cambio','forma'},
                                    'tamaño':{'talla','grande','agrandar','agrando','achicar','achico','hacer','hago','pequeño','pequeña'},
                                    'borrar formato':{'quito','quitar','formato','borro','borrar'},
                                    'negrita':{'gordo','gordita','gruezo','grueza'},
                                    'cursiva':{'inclino','letra','inclinada','chueca'},
                                    'subrayado':{'subrayo','subrrayo','subrayaba','subrrayaba','raya', 'abajo','rayita'}},
                    'paragraph':{}},
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
    answer = ''
    
    for n in DFlamis:
        for m in DFlamis[n]:
            for o in DFlamis[n][m]:

                set_d = DFlamis[n][m][o]

                if skh.is_bigger(variable,len(set_m & set_d)):
                    variable = len(set_m & set_d)

                    answer = skh.sentence_starter()+' ' + n + ' ' + skh.second() + ' ' + m + ' ' + skh.more_conncectors() + ' ' + skh.conncetors() + ' ' + o

    return answer
