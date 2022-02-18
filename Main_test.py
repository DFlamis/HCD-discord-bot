import Saki_Helper as skh

a = 'oigan, saben como copiar el formato??'
a = a.replace('?','').replace(',','')
b = a.split(' ')

c = set(b)

print(f'->{c}')

base = []

orasion = ''

DFlamis = {'home':{'clipboard':['copiar','pegar','copiar formato','cortar','formato'],'font':['negrita','cursiva','subrayado'],'paragraph':['hols']},'solo':{'Aclipboard':['copiar','pegar','copiar formato','cortar','formato'],'Afont':['negrita','cursiva','subrayado'],'Aparagraph':['hols']}}
for n in DFlamis:
    for m in DFlamis[n]:
        print(DFlamis[n][m])
        
        d = set(DFlamis[n][m])
        print(f'-->{d}')
        print(f'---->{d&c}')
        print(f'---->{len(d&c)}')
        print(f'---->{list(d&c)}')
        print(f'------>{n,m}')

        if skh.is_bigger(len(base),len(d&c)):
    
            print(f'>>>>>{len(base)}')

            print(skh.is_bigger(len(base),len(d&c)))

            base = list(d&c)
            orasion = skh.sentence_starter()+' ' + n + ' ' + skh.second() + ' ' + m

print(orasion)
