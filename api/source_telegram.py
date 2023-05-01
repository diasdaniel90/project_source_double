import configparser
import json
from datetime import datetime
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.functions.messages import (SearchRequest)
from telethon.tl.types import PeerChannel
from telethon.tl.types import (InputMessagesFilterEmpty)
#from telethon import types
import re
from api import util
#from api import regex_telegram 
from django.conf import settings


# Reading Configs
config = configparser.ConfigParser()
#config.read("api/config-telegram.ini")
# Setting configuration values
api_id = settings.TELEGRAM_ENV['API_ID']
api_hash = settings.TELEGRAM_ENV['API_HASH']
#api_hash = str(api_hash)
api_channel = settings.TELEGRAM_ENV['API_CHANNEL']
phone = settings.TELEGRAM_ENV['PHONE']
username = settings.TELEGRAM_ENV['USERNAME']
source_t_1 = settings.TELEGRAM_ENV['SOURCE_T_1']
source_t_2 = settings.TELEGRAM_ENV['SOURCE_T_2']
source_t_3 = settings.TELEGRAM_ENV['SOURCE_T_3']
source_t_4 = settings.TELEGRAM_ENV['SOURCE_T_4']
source_t_5 = settings.TELEGRAM_ENV['SOURCE_T_5']
source_t_6 = settings.TELEGRAM_ENV['SOURCE_T_6']
source_t_7 = settings.TELEGRAM_ENV['SOURCE_T_7']
source_t_8 = settings.TELEGRAM_ENV['SOURCE_T_8']
source_t_9 = settings.TELEGRAM_ENV['SOURCE_T_9']

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)

# diferenca = timedelta(hours=-3)
# fuso_horario = timezone(diferenca)

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
    client.start()  
    
    @client.on(events.NewMessage(chats=source_t_1))
    async def my_event_handler(event):
        source=source_t_1
        print("-------------------------------------------")
        #print(util.timestemp_to_string(timestamp))
        #print(event.raw_text)
        #strs = re.sub(r"[^a-zA-Z0-9: \n]","",event.raw_text)
        print(event.raw_text)
        strs = re.sub(r"[^a-zA-Z0-9🔴⚪️ ⚫️\n]","",event.raw_text)
        print(strs)
        timestamp = datetime.timestamp(event.date)
        #print(util.timestemp_to_string(timestamp))
        if re.search('entre', strs,re.IGNORECASE) or re.search('entrar', strs,re.IGNORECASE):  
            if re.search('vermelho', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": source})
                print(json_send)
                util.send_cliente_sinals(json_send)
            elif re.search('preto', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": source})
                print(json_send)
                util.send_cliente_sinals(json_send)
            else:
                print(strs)
                print("########not sinal##########") 
        
    @client.on(events.NewMessage(chats=source_t_9))
    async def my_event_handler(event):
        source=source_t_9                                   
        print("-------------------------------------------")
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
                json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": source})
                print(json_send)
                util.send_cliente_sinals(json_send)
            elif re.search('preto', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": source})
                print(json_send)
                util.send_cliente_sinals(json_send)
            else:
                print(strs)
                print("########not sinal##########")         
                  
    @client.on(events.NewMessage(chats=source_t_8)) 
    async def my_event_handler(event):
        source=source_t_8                                  
        #print("-------------------------------------------")
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
                json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": source})
                print(json_send)
                util.send_cliente_sinals(json_send)
            elif re.search('preto', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": source})
                print(json_send)
                util.send_cliente_sinals(json_send)
            else:
                print(strs)
                print("########not sinal##########") 

    @client.on(events.NewMessage(chats=source_t_6)) 
    async def my_event_handler(event):
        source=source_t_6                        
        #print(event.raw_text)       
        strs = re.sub(r"[^a-zA-Z0-9\n']","",event.raw_text)
        #print(strs[0])
        line = strs.split("\n")
        #print(line[0])
        strs = line[0]
        timestamp = timestamp = datetime.timestamp(event.date)
        #print(util.timestemp_to_string(timestamp))
        if re.search('entrarno', strs,re.IGNORECASE) and re.search('Apso', strs,re.IGNORECASE):  
            if re.search('vermelho', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": source})
                print(json_send)
                util.send_cliente_sinals(json_send)
            elif re.search('black', strs,re.IGNORECASE) :
                json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": source})
                print(json_send)
                util.send_cliente_sinals(json_send)
            else:
                print(timestamp)
                print(strs)
                print("########not sinal##########")

    @client.on(events.NewMessage(chats=source_t_3))
    async def my_event_handler(event):
        source=source_t_3
        #print(event.raw_text)
        #print("-------")
        strs = re.sub(r"[^a-zA-Z0-9⚫️🔴']","",event.raw_text)
        #print(strs)
        timestamp = timestamp = datetime.timestamp(event.date)
        #print(util.timestemp_to_string(timestamp))
        if re.search('EntradaConfirmadaAtG2Entrada', strs,re.IGNORECASE) and re.search('Apsonum', strs,re.IGNORECASE):  
            if re.search('🔴', strs,re.IGNORECASE): #and re.search('vermelho', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": source})
                #print(json_send)
                util.send_cliente_sinals(json_send)
            elif re.search('⚫️', strs,re.IGNORECASE): #and re.search('preto', strs,re.IGNORECASE) :
                json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": source})
                #print(json_send)
                util.send_cliente_sinals(json_send)
            else:
                #print(strs)
                print("########not sinal##########")  
    
    @client.on(events.NewMessage(chats=source_t_4))
    async def my_event_handler(event):
        source=source_t_4
        #print("-------------------------------------------")
        #print(event.raw_text)
        strs = re.sub(r"[^a-zA-Z0-9🔴⚪️ ⚫️\n]","",event.raw_text)
        timestamp = timestamp = datetime.timestamp(event.date)
        #print(util.timestemp_to_string(timestamp))
        if re.search('entre', strs,re.IGNORECASE) or re.search('entrar', strs,re.IGNORECASE):  
            if re.search('vermelho', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": source})
                #print(json_send)
                util.send_cliente_sinals(json_send)
            elif re.search('preto', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": source})
                #print(json_send)
                util.send_cliente_sinals(json_send)
            else:
                #print(strs)
                print("########not sinal##########")         
                                        
    @client.on(events.NewMessage(chats=source_t_5)) 
    async def my_event_handler(event):
        source=source_t_5
        #print("-------------------------------------------")
        timestamp = timestamp = datetime.timestamp(event.date)
        #print(util.timestemp_to_string(timestamp))
        strs = re.sub(r"[^a-zA-Z0-9🔴⚪️ ⚫️]","",event.raw_text)
        print(strs)
        timestamp = timestamp = datetime.timestamp(event.date)
        if re.search('realizar at', strs,re.IGNORECASE) and re.search('entrar', strs,re.IGNORECASE):  
            if re.search('vermelho', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": source})
                #print(json_send)
                util.send_cliente_sinals(json_send)
            elif re.search('preto', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": source})
                #print(json_send)
                util.send_cliente_sinals(json_send)
            else:
                #print(strs)
                print("########not sinal##########") 

    @client.on(events.NewMessage(chats=source_t_2)) 
    async def my_event_handler(event):
        source=source_t_2
        #print("-------------------------------------------")
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
                json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": source})
                print(json_send)
                util.send_cliente_sinals(json_send)
            elif re.search('preto', strs,re.IGNORECASE):
                json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": source})
                print(json_send)
                util.send_cliente_sinals(json_send)
            else:
                #print(strs)
                print("########not sinal##########") 

    # @client.on(events.NewMessage(chats=)) 
    # async def my_event_handler(event):
    #     #print("-------------------------------------------")
    #     timestamp = timestamp = datetime.timestamp(event.date)
    #     #print(util.timestemp_to_string(timestamp))
    #     strs = re.sub(r"[^a-zA-Z0-9:\n]","",event.raw_text)
    #     if re.search('POSSVELBRANCO', strs,re.IGNORECASE) and re.search('Entre', strs,re.IGNORECASE):  
    #         dict_channel_b = {}
    #         line = strs.split("\n")
    #         line.pop()
    #         for item in line:
    #             if ':' in item:
    #                 dict_channel_b.update({item:{'hora': item,'color':0,'branco': 0}})
    #                 print(item)
    #         json_send = json.dumps({"source": "", "type": "list" , "time":timestamp, "sinals": dict_channel_b})
    #         print(json_send)
    #         util.send_cliente_sinals(json_send)    

    # @client.on(events.NewMessage(chats=)) 
    # async def my_event_handler(event):
    #     #print("-------------------------------------------")
    #     timestamp = timestamp = datetime.timestamp(event.date)
    #     #print(util.timestemp_to_string(timestamp))
    #     strs = re.sub(r"[^a-zA-Z0-9🔴⚪️ ⚫️]","",event.raw_text)
    #     #print(strs)
    #     if re.search('CHANCE DE BRANCO', strs,re.IGNORECASE) and re.search('', strs,re.IGNORECASE):  
    #         dict_channel = regex_telegram.channel_a(event.raw_text)
    #         json_send = json.dumps({"source": "", "type": "list" , "time":timestamp, "sinals": dict_channel})
    #         #print(json_send)
    #         util.send_cliente_sinals(json_send)

    # @client.on(events.NewMessage(chats=)) #
    # async def my_event_handler(event):
    #     #print(event.raw_text)
    #     print("-------")
    #     print("")
    #     strsaux = re.sub(r"[^a-zA-Z0-9⬛️🟥\n']","",event.raw_text)
    #     #print(strs[0])
    #     line = strsaux.split("\n")
    #     #print(line[0])
    #     strs = line[0]
    #     timestamp = timestamp = datetime.timestamp(event.date)
    #     print(util.timestemp_to_string(timestamp))
    #     if re.search('apostarno', strs,re.IGNORECASE):# #and re.search('realizarat', strs,re.IGNORECASE):  
    #         if re.search('🟥', strs,re.IGNORECASE) and re.search('vermelho', strs,re.IGNORECASE):
    #             json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": ""})
    #             print(json_send)
    #             util.send_cliente_sinals(json_send)
    #         elif re.search('⬛', strs,re.IGNORECASE): #and re.search('preto', strs,re.IGNORECASE) :
    #             json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": ""})
    #             print(json_send)
    #             util.send_cliente_sinals(json_send)
    #         else:
    #             print("event",event.raw_text)
    #             print(timestamp)
    #             print(strs)
    #             print("########not sinal##########")   
                                   
    # @client.on(events.NewMessage(chats=)) 
    # async def my_event_handler(event):
    #     print("-----------------------------------------------------------")
    #     strs = re.sub(r"[^a-zA-Z0-9🔴⚪️ ⚫️]","",event.raw_text)
    #     timestamp = timestamp = datetime.timestamp(event.date)
    #     if re.search('entre', strs,re.IGNORECASE) or re.search('entrar', strs,re.IGNORECASE):  
    #         if re.search('vermelho', strs,re.IGNORECASE):
    #             #json_send = json.dumps({"time":timestamp, "color": 1, "source": ""})
    #             print(" VAI NO VERMELHO")
    #         elif re.search('preto', strs,re.IGNORECASE):
    #             #json_send = json.dumps({"time":timestamp, "color": 2, "source": ""})
    #             print(" VAI NO PRETO")
    #         else:
    #             print("########not sinal##########")
                                         
    # @client.on(events.NewMessage(chats=)) 
    # async def my_event_handler(event):
    #     #print("-------------------------------------------")
    #     #print("")
    #     strs = re.sub(r"[^a-zA-Z0-9🔴⚫️𝗔-𝗨']","",event.raw_text)
    #     #print(strs)
    #     timestamp = timestamp = datetime.timestamp(event.date)
    #     #print(util.timestemp_to_string(timestamp))
    #     if re.search('𝗖𝗢𝗥𝗗𝗔𝗔𝗣𝗢𝗦𝗧𝗔', strs,re.IGNORECASE) and re.search('𝗝𝗢𝗚𝗔𝗥', strs,re.IGNORECASE):  
    #         if re.search('🔴', strs,re.IGNORECASE):
    #             json_send = json.dumps({"type": "real_time",  "time":timestamp, "color": 1, "source": ""})
    #             #print(json_send)
    #             util.send_cliente_sinals(json_send)
    #         elif re.search('⚫️', strs,re.IGNORECASE):
    #             json_send = json.dumps({"type": "real_time" , "time":timestamp, "color": 2, "source": ""})
    #             #print(json_send)
    #             util.send_cliente_sinals(json_send)
    #         else:
    #             #print(strs)
    #             print("########not sinal##########")  

    client.run_until_disconnected()

