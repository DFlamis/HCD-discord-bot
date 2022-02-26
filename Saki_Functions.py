import Saki_Helper as skh

#Looking for 
def finder(mensaje):
    office = ['word','power point','excel']
    words = mensaje.split(' ')
    for n in words:
        if n.lower() in office:
            return True,n.lower()
    return False,'None'

#This function return the full answer
def sentence_builder(simple_answer):
    n = 3
    key_words = simple_answer.split(' ')

    answer = skh.sentence_starter()+' '+key_words[0]+', '+skh.second()+' '+key_words[1]+', '+skh.more_conncectors()+' '+skh.conncetors()+' '+key_words[2]

    times = len(key_words)

    if times > 3: #Continuar creando oraciones cuando esta dentro de las opciones de un boton
        while(n < times):
            answer = answer+', '+skh.more_conncectors()+' '+skh.conncetors()+' '+key_words[n]
            n = n + 1

    return answer.replace('-',' ')

#Experimental---------------------------------------------------------------------------------------
def match(message,DFlamis):
    list_TM = message.split(' ')

    set_m = set(list_TM)
    variable = 0
    answers = ''
    
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

                                    answers = n+' '+m+' '+o+' '+p+' '+q

                        else:
                            set_d = DFlamis[n][m][o][p]

                            if skh.is_bigger(variable,len(set_m & set_d)):
                                variable = len(set_m & set_d)

                                answers = n+' '+m+' '+o+' '+p

                else: #El boton no tiene mas opciones

                    set_d = DFlamis[n][m][o]

                    if skh.is_bigger(variable,len(set_m & set_d)):
                        variable = len(set_m & set_d)

                        answers = n+' '+m+' '+o

    return answers
#Experimental---------------------------------------------------------------------------------------

#Delete useless characters
def message_cleanner(message):
    serylda = no_punctuation_mark(message)
    lissandra = no_accent_mark(serylda)
    avarosa = lissandra.lower()
    return avarosa

def no_punctuation_mark(message):
    marks = ['¿','?','¡','!',',','.',';',':']
    for mark in marks:
        message = message.replace(mark,'')
    return message

def no_accent_mark(message):
    true_message = message.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
    return true_message
