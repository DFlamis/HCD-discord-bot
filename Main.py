import discord
import Saki_Functions as skf
import Saki_Helper as skh

client = discord.Client()

Call_sign = '!hcd'

#Start
@client.event
async def on_ready():
    print('Listoh papuh, iniciado como {0.user}'.format(client))

#Recive mensajes
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #Shortcuts
    msg_received = message.content
    msg_send = message.channel.send
    
    msg_a = 'Inicie'

    #Reply
    if msg_received.startswith(Call_sign):

        #Experimental!-------------------------------------------------
        testoo = skf.finder(msg_received)
        if testoo[0]:
            msg_a = testoo[1]
        else:
            msg_a = testoo[1]

        #Experimental!-------------------------------------------------

        #message builder
        msg_final = skh.sentence_starter() + '.'

        #Reply
        await msg_send(msg_a)

client.run('TOKEN')
