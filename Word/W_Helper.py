import Saki_Helper as skh

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
            'insert':{},
            'draw':{},
            'design':{},
            'layout':{'configurar páginas':{'márgenes':{},
                                            'orientacion':{},
                                            'tamaño':{},
                                            'columnas':{'una':{'un','una','columna','1'},
                                                        'dos':{'dos','columna','columnas','2'},
                                                        'tres':{'tres','columna','columnas','3'},
                                                        'más columnas':{'número de columnas':{'columna','columnas','varias','cuatro','cinco','muchas'},
                                                                        'línea entre columnas':{'raya','rayita','entre','enmedio','medio','columna','columnas','linea','lineas','liniesita'}}},
                                            'saltos':{}},
                        'párrafo':{},
                        'organizar':{}},
            'references':{},
            'mailings':{},
            'reviews':{}}


def match(message):
    #Remove useless characters
    list_TM = message.split(' ')

    set_m = set(list_TM)
    variable = 0
    answer = ''
    
    for n in DFlamis: #Ribbon Tabs
        for m in DFlamis[n]: #Group Tabs
            for o in DFlamis[n][m]: #Buttoms

                if skh.more_options(DFlamis[n][m][o]): #Evitar error por falta de indice

                    for p in DFlamis[n][m][o]: #Option Box

                        if skh.more_options(DFlamis[n][m][o][p]): #Evitar error por falta de indice

                            for q in DFlamis[n][m][o][p]: #More options
                                
                                set_d = DFlamis[n][m][o][p][q]

                                if skh.is_bigger(variable,len(set_m & set_d)):
                                    variable = len(set_m & set_d)

                                    answer = skh.sentence_starter()+' ' + n + ' ' + skh.second() + ' ' + m + ' ' + skh.more_conncectors() + ' ' + skh.conncetors() + ' ' + o + ' ' + skh.more_conncectors() + ' ' + skh.conncetors() + ' ' + p  + ' ' + skh.more_conncectors() + ' ' + skh.conncetors() + ' ' + q

                        else:
                            set_d = DFlamis[n][m][o][p]

                            if skh.is_bigger(variable,len(set_m & set_d)):
                                variable = len(set_m & set_d)

                                answer = skh.sentence_starter()+' ' + n + ' ' + skh.second() + ' ' + m + ' ' + skh.more_conncectors() + ' ' + skh.conncetors() + ' ' + o  + ' ' + skh.more_conncectors() + ' ' + skh.conncetors() + ' ' + p

                else: #El boton no tiene mas opciones

                    set_d = DFlamis[n][m][o]

                    if skh.is_bigger(variable,len(set_m & set_d)):
                        variable = len(set_m & set_d)

                        answer = skh.sentence_starter()+' ' + n + ' ' + skh.second() + ' ' + m + ' ' + skh.more_conncectors() + ' ' + skh.conncetors() + ' ' + o

    return answer