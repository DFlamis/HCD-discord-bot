#Look for 
def finder(mensaje):
    office = ['word','power point','excel']
    words = mensaje.split(' ')
    for n in words:
        if n.lower() in office:
            return True,n.lower()
    return False,'None'