from cgitb import text
import Saki_Functions as sk
import Saki_Helper as skh

testo = input('Tiene alguna duda?: ')
answer = sk.finder(testo)
print(answer)

print(skh.saludo)
