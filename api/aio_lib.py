import csv
import aiofiles
from aiocsv import AsyncDictWriter,AsyncWriter
import aiohttp
import asyncio
from api import get_config
import json



# async def save(dicio,collection):
#     async with aiofiles.open(collection+".csv", mode="a", encoding="utf-8", newline="") as afp:
#         writer = AsyncDictWriter(afp, dicio.keys(), restval="NULL", quoting=csv.QUOTE_ALL)
#         #await writer.writeheader()
#         await writer.writerow(dicio)   

async def save_list_obj(lista, collection):
    async with aiofiles.open(collection+".csv", mode="a", encoding="utf-8", newline="") as afp:
        writer = AsyncDictWriter(afp, lista[0].__dict__, restval="NULL", quoting=csv.QUOTE_ALL)
        #await writers.writeheader()
        for dicionario in lista:   
            print("save_list:",dicionario.__dict__)     
            await writer.writerow(dicionario.__dict__)  

        
# async def save_dicts_to_list(dicionario, collection):
#     async with aiofiles.open(collection+".csv", mode="a", encoding="utf-8", newline="") as afp:
#         writer = AsyncWriter(afp, dialect="unix")
#         print("save_dicts_to_list:",list(dicionario.values()))
#         for lista in list(dicionario.values()):   
#             await writer.writerow(list(lista.values()))

        #await writer.writerows([["John", 26], ["Sasha", 42], ["Hana", 37]])    
        
async def play_bet(item):
    # item.status_bet = 'created'
    payload_ = {"amount":str(item.amount),"currency_type":"BRL","color":float(item.color),"free_bet":False,"wallet_id":get_config.wallet}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://blaze.com/api/roulette_bets',headers=get_config.header_api,json=payload_) as resp:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",await resp.text())
            json_ = json.loads(await resp.text())
            if json_.get('bet'):
                item.status_bet = json_.get('bet').get('status')




