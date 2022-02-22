import discord

import Saki_Functions as skf
import Saki_Helper as skh

import Word.W_Helper as wh

client = discord.Client()

Call_sign = '!hcd'

#Start
@client.event
async def on_ready():
    print('Saki assistant started as: {0.user}'.format(client))

#Recive mensajes
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #Shortcuts
    msg_received = message.content
    msg_send = message.channel.send
    
    msg_final = 'Empty'

    #Reply
    if msg_received.startswith(Call_sign):

        #Saki IA (DO NOT DELETE!!)
        true_message = skh.message_cleanner(msg_received)

        saki = skf.finder(true_message)
        if saki[0]:
            if saki[1] == 'word':
                simple_answer = wh.match(true_message)
                msg_final = skf.sentence_builder(simple_answer)

            elif saki[1] == 'excel':
                msg_final = 'Excel'

            elif saki[1] == 'power point':
                msg_final = 'Power Point'
                
            else:
                msg_final = 'Empty++'
        else:
            msg_final = 'No c xd'

        #Reply
        await msg_send(msg_final)

client.run('TOKEN')
