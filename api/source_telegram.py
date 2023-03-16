import configparser
import json
from datetime import datetime, timezone,timedelta
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.functions.messages import (SearchRequest)
from telethon.tl.types import PeerChannel
from telethon.tl.types import (InputMessagesFilterEmpty)
#from telethon import types
import re
from api import util
from api import regex_telegram 
# Reading Configs
config = configparser.ConfigParser()
config.read("api/config-telegram.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
api_channel = config['Telegram']['api_channel']
api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)

diferenca = timedelta(hours=-3)
fuso_horario = timezone(diferenca)

async def main(phone):
    await client.start()
    print("Client Created")
    # Ensure you're authorized
    if await client.is_user_authorized() == False:
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

    me = await client.get_me()
    # entity = PeerChannel(int(api_channel))
    # my_channel = await client.get_entity(entity)
 
    # print(entity)
    # print(my_channel)

with client:
    client.loop.run_until_complete(main(phone))
    
    banner = """
    ┌─┐┌─┐┌┬┐┌─┐┬ ┬  ┬  ┬┬┬  ┬┌─┐  
    ├┤ └─┐ │ │ ││ │  └┐┌┘│└┐┌┘│ │  
    └─┘└─┘ ┴ └─┘└─┘   └┘ ┴ └┘ └─┘  
    """  
    print(banner)
    client.start()  #5419023244
                                      #BOTTELEGRAM   5419023244    
    @client.on(events.NewMessage(chats=5419023244)) #BOTTELEGRAM 
    async def my_event_handler(event):
        print("-------------------------------------------")
        #print("BOTTELEGRAM")
        #print(util.timestemp_to_string(timestamp))
        #print(event.raw_text)
        #strs = re.sub(r"[^a-zA-Z0-9: \n]","",event.raw_text)
        #print(event.raw_text)
        strs = re.sub(r"[^a-zA-Z0-9🔴⚪️ ⚫️\n]","",event.raw_text)
        print(strs)
        timestamp = datetime.timestamp(event.date)
        #print(util.timestemp_to_string(timestamp))
        if re.search('entre', strs,re.IGNORECASE) or re.search('entrar', strs,re.IGNORECASE):  
            if re.search('vermelho', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": "BOTTELEGRAM"})
                print(json_send)
                util.send_cliente_sinals(json_send)
            elif re.search('preto', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": "BOTTELEGRAM"})
                print(json_send)
                util.send_cliente_sinals(json_send)
            else:
                print(strs)
                print("########not sinal##########") 
        
                                      #BOTTELEGRAM  depois_do_sol 6294450052    
    @client.on(events.NewMessage(chats=6294450052)) #BOTTELEGRAM 
    async def my_event_handler(event):
        print("-------------------------------------------")
        #print("BOTTELEGRAM")
        #print(util.timestemp_to_string(timestamp))
        #print(event.raw_text)
        #strs = re.sub(r"[^a-zA-Z0-9: \n]","",event.raw_text)
        #print(event.raw_text)
        strs = re.sub(r"[^a-zA-Z0-9🔴⚪️ ⚫️\n]","",event.raw_text)
        print(strs)
        timestamp = datetime.timestamp(event.date)
        #print(util.timestemp_to_string(timestamp))
        if re.search('entre', strs,re.IGNORECASE) or re.search('entrar', strs,re.IGNORECASE):  
            if re.search('vermelho', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": "depois_do_sol"})
                print(json_send)
                util.send_cliente_sinals(json_send)
            elif re.search('preto', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": "depois_do_sol"})
                print(json_send)
                util.send_cliente_sinals(json_send)
            else:
                print(strs)
                print("########not sinal##########")         
        
        
        
                                    
    @client.on(events.NewMessage(chats=1844400705)) #quebrancoablaze
    async def my_event_handler(event):
        #print("-------------------------------------------")
        #print("quebrancoablaze")
        timestamp = timestamp = datetime.timestamp(event.date)
        #print(util.timestemp_to_string(timestamp))
        #print(event.raw_text)
        #strs = re.sub(r"[^a-zA-Z0-9: \n]","",event.raw_text)
        #print(event.raw_text)
        strs = re.sub(r"[^a-zA-Z0-9🔴⚪️ ⚫️\n]","",event.raw_text)
        #print(strs)
        #print(util.timestemp_to_string(timestamp))
        if re.search('entre', strs,re.IGNORECASE) or re.search('entrar', strs,re.IGNORECASE):  
            if re.search('vermelho', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": "quebrancoablaze"})
                print(json_send)
                util.send_cliente_sinals(json_send)
            elif re.search('preto', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": "quebrancoablaze"})
                print(json_send)
                util.send_cliente_sinals(json_send)
            else:
                print(strs)
                print("quebrancoablaze") 
                print("########not sinal##########") 


    @client.on(events.NewMessage(chats=1642769661)) #BLAZE OFICIAL TENDÊNCIA DE BRANCO
    async def my_event_handler(event):
        #print("-------------------------------------------")
        #print("#BLAZE OFICIAL TENDÊNCIA DE BRANCO")
        timestamp = timestamp = datetime.timestamp(event.date)
        #print(util.timestemp_to_string(timestamp))
        strs = re.sub(r"[^a-zA-Z0-9:\n]","",event.raw_text)
        if re.search('POSSVELBRANCO', strs,re.IGNORECASE) and re.search('Entre', strs,re.IGNORECASE):  
            dict_channel_b = {}
            line = strs.split("\n")
            line.pop()
            for item in line:
                if ':' in item:
                    dict_channel_b.update({item:{'hora': item,'color':0,'branco': 0}})
                    print(item)
            json_send = json.dumps({"source": "brancoofical", "type": "list" , "time":timestamp, "sinals": dict_channel_b})
            print(json_send)
            util.send_cliente_sinals(json_send)    

    @client.on(events.NewMessage(chats=1570776802)) #BLAZE OFICIAL DOUBLE VIP
    async def my_event_handler(event):
        #print(event.raw_text)
        #print("-------")
        #print("BLAZE OFICIAL DOUBLE VIP")
        
        strs = re.sub(r"[^a-zA-Z0-9\n']","",event.raw_text)
        #print(strs[0])
        line = strs.split("\n")
        #print(line[0])
        strs = line[0]
        timestamp = timestamp = datetime.timestamp(event.date)
        #print(util.timestemp_to_string(timestamp))
        if re.search('entrarno', strs,re.IGNORECASE) and re.search('Apso', strs,re.IGNORECASE):  
            if re.search('vermelho', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": "BLAZE OFICIAL DOUBLE VIP"})
                print(json_send)
                util.send_cliente_sinals(json_send)
            elif re.search('black', strs,re.IGNORECASE) :
                json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": "BLAZE OFICIAL DOUBLE VIP"})
                print(json_send)
                util.send_cliente_sinals(json_send)
            else:
                print("channel:BLAZE OFICIAL DOUBLE VIP 1570776802")
                print(timestamp)
                print(strs)
                print("########not sinal##########")

    @client.on(events.NewMessage(chats=1361655475)) #doubleimperial
    async def my_event_handler(event):
        #print(event.raw_text)
        #print("-------")
        #print("doubleimperial")
        strs = re.sub(r"[^a-zA-Z0-9⚫️🔴']","",event.raw_text)
        #print(strs)
        timestamp = timestamp = datetime.timestamp(event.date)
        #print(util.timestemp_to_string(timestamp))
        if re.search('EntradaConfirmadaAtG2Entrada', strs,re.IGNORECASE) and re.search('Apsonum', strs,re.IGNORECASE):  
            if re.search('🔴', strs,re.IGNORECASE): #and re.search('vermelho', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": "doubleimperial"})
                #print(json_send)
                util.send_cliente_sinals(json_send)
            elif re.search('⚫️', strs,re.IGNORECASE): #and re.search('preto', strs,re.IGNORECASE) :
                json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": "doubleimperial"})
                #print(json_send)
                util.send_cliente_sinals(json_send)
            else:
                #print(strs)
                print("########not sinal##########")  

    # @client.on(events.NewMessage(chats=1583192657)) #robodouble
    # async def my_event_handler(event):
    #     #print(event.raw_text)
    #     print("-------")
    #     print("robodouble")

        
    #     strsaux = re.sub(r"[^a-zA-Z0-9⬛️🟥\n']","",event.raw_text)
    #     #print(strs[0])
    #     line = strsaux.split("\n")
    #     #print(line[0])
    #     strs = line[0]
    #     timestamp = timestamp = datetime.timestamp(event.date)
    #     print(util.timestemp_to_string(timestamp))
    #     if re.search('apostarno', strs,re.IGNORECASE):# #and re.search('realizarat', strs,re.IGNORECASE):  
    #         if re.search('🟥', strs,re.IGNORECASE) and re.search('vermelho', strs,re.IGNORECASE):
    #             json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": "robodouble"})
    #             print(json_send)
    #             util.send_cliente_sinals(json_send)
    #         elif re.search('⬛', strs,re.IGNORECASE): #and re.search('preto', strs,re.IGNORECASE) :
    #             json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": "robodouble"})
    #             print(json_send)
    #             util.send_cliente_sinals(json_send)
    #         else:
    #             print("event",event.raw_text)
    #             print("channel:robodouble 1583192657")
    #             print(timestamp)
    #             print(strs)
    #             print("########not sinal##########")   


                                        #1528717490 
    # @client.on(events.NewMessage(chats=1528717490)) #CARLINHOS #FRESS
    # async def my_event_handler(event):
    #     print("-----------------------------------------------------------")
    #     strs = re.sub(r"[^a-zA-Z0-9🔴⚪️ ⚫️]","",event.raw_text)
    #     timestamp = timestamp = datetime.timestamp(event.date)

    #     if re.search('entre', strs,re.IGNORECASE) or re.search('entrar', strs,re.IGNORECASE):  
    #         if re.search('vermelho', strs,re.IGNORECASE):
    #             #json_send = json.dumps({"time":timestamp, "color": 1, "source": "CARLINHOS"})
    #             print("CARLINHOS VAI NO VERMELHO")
    #         elif re.search('preto', strs,re.IGNORECASE):
    #             #json_send = json.dumps({"time":timestamp, "color": 2, "source": "CARLINHOS"})
    #             print("CARLINHOS VAI NO PRETO")
    #         else:
    #             print("########not sinal##########")
    
                                      
    @client.on(events.NewMessage(chats=1785855192)) #trovaovip
    async def my_event_handler(event):
        #print("-------------------------------------------")
        #print("trovaovip")

        strs = re.sub(r"[^a-zA-Z0-9🔴⚫️𝗔-𝗨']","",event.raw_text)
        #print(strs)
        timestamp = timestamp = datetime.timestamp(event.date)
        #print(util.timestemp_to_string(timestamp))
        if re.search('𝗖𝗢𝗥𝗗𝗔𝗔𝗣𝗢𝗦𝗧𝗔', strs,re.IGNORECASE) and re.search('𝗝𝗢𝗚𝗔𝗥', strs,re.IGNORECASE):  
            if re.search('🔴', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": "trovaovip"})
                #print(json_send)
                util.send_cliente_sinals(json_send)
            elif re.search('⚫️', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": "trovaovip"})
                #print(json_send)
                util.send_cliente_sinals(json_send)
            else:
                #print(strs)
                print("########not sinal##########")            

    
    @client.on(events.NewMessage(chats=1461554132)) #Sinais Double          1461554132
    async def my_event_handler(event):
        #print("-------------------------------------------")
        #print("Sinais Double VITALICIO")
        #print(event.raw_text)
        strs = re.sub(r"[^a-zA-Z0-9🔴⚪️ ⚫️\n]","",event.raw_text)
        timestamp = timestamp = datetime.timestamp(event.date)
        #print(util.timestemp_to_string(timestamp))
        if re.search('entre', strs,re.IGNORECASE) or re.search('entrar', strs,re.IGNORECASE):  
            if re.search('vermelho', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": "Sinais Double"})
                #print(json_send)
                util.send_cliente_sinals(json_send)
            elif re.search('preto', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": "Sinais Double"})
                #print(json_send)
                util.send_cliente_sinals(json_send)
            else:
                #print(strs)
                print("########not sinal##########")         
                                        #1725615740
    @client.on(events.NewMessage(chats=1725615740)) #aglair
    async def my_event_handler(event):
        #print("-------------------------------------------")
        #print("aglair")
        timestamp = timestamp = datetime.timestamp(event.date)
        #print(util.timestemp_to_string(timestamp))
        strs = re.sub(r"[^a-zA-Z0-9🔴⚪️ ⚫️]","",event.raw_text)
        #print(strs)
        if re.search('CHANCE DE BRANCO', strs,re.IGNORECASE) and re.search('LISTA DOUBLE AGLAIR BLAZE VIP', strs,re.IGNORECASE):  
            dict_channel = regex_telegram.channel_aglair(event.raw_text)
            json_send = json.dumps({"source": "aglair", "type": "list" , "time":timestamp, "sinals": dict_channel})
            #print(json_send)
            util.send_cliente_sinals(json_send)


    @client.on(events.NewMessage(chats=1642155096)) #Sinais Blaze Double 24hrs   1642155096
    async def my_event_handler(event):
        #print("-------------------------------------------")
        print("vip24hrs")
        timestamp = timestamp = datetime.timestamp(event.date)
        #print(util.timestemp_to_string(timestamp))

        strs = re.sub(r"[^a-zA-Z0-9🔴⚪️ ⚫️]","",event.raw_text)
        print(strs)
        timestamp = timestamp = datetime.timestamp(event.date)
        if re.search('realizar at', strs,re.IGNORECASE) and re.search('entrar', strs,re.IGNORECASE):  
            if re.search('vermelho', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": "vip24hrs"})
                #print(json_send)
                util.send_cliente_sinals(json_send)
            elif re.search('preto', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": "vip24hrs"})
                #print(json_send)
                util.send_cliente_sinals(json_send)
            else:
                #print(strs)
                print("########not sinal##########") 

                                     #MASTER BLAZE OFICIAL   1755113665    
    @client.on(events.NewMessage(chats=1755113665)) #MASTER BLAZE OFICIAL 
    async def my_event_handler(event):
        #print("-------------------------------------------")
        #print("MASTER BLAZE OFICIAL")
        timestamp = timestamp = datetime.timestamp(event.date)
        #print(util.timestemp_to_string(timestamp))
        #print(event.raw_text)
        #strs = re.sub(r"[^a-zA-Z0-9: \n]","",event.raw_text)
        #print(event.raw_text)
        strs = re.sub(r"[^a-zA-Z0-9🔴⚪️ ⚫️\n]","",event.raw_text)
        #print(strs)
        timestamp = timestamp = datetime.timestamp(event.date)
        #print(util.timestemp_to_string(timestamp))
        if re.search('entre', strs,re.IGNORECASE) or re.search('entrar', strs,re.IGNORECASE):  
            if re.search('vermelho', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": "MASTER BLAZE OFICIAL "})
                #print(json_send)
                util.send_cliente_sinals(json_send)
            elif re.search('preto', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": "MASTER BLAZE OFICIAL "})
                #print(json_send)
                util.send_cliente_sinals(json_send)
            else:
                #print(strs)
                print("########not sinal##########") 



    client.run_until_disconnected()

