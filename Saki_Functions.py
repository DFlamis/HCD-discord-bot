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

    if times > 3:
        while(n < times):
            answer = answer+', '+skh.more_conncectors()+' '+skh.conncetors()+' '+key_words[n]
            n = n + 1

    return answer
