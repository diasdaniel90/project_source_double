import asyncio
import json
#from multiprocessing.connection import wait
from api import aio_lib
from api.class_async import cache_async, ValidBet
from api import util
from api import get_config
import time

async def coroutine_task_status_status(message_status):
    if message_status['bet_status'] == 'waiting':
        obj_cache_id.set_id_bet(message_status['ID_bet'])
        print("obj_cache_id.ID_bet",obj_cache_id.ID_bet)
        print("====================INICIO==================================")
        print('+++++PRONTO PARA APOSTAR: %s' % (message_status))
        #await asyncio.sleep(get_config.process_time)
        #time.sleep(3)
        #await asyncio.sleep(3)
        print("FIM DA ESPERA DE:",3)
        
        #obj_cache_.convert_sinal_list_to_bet(message_status)
        obj_cache_.convert_sinal_to_bet(message_status)

        if obj_cache_.list_bets_sinals:
            #obj_cache_.score_bet()
            #obj_cache_.convert_score_bet(message_status)
            #print("ID_bet",message_status['ID_bet'])
            obj_cache_.set_id(message_status['ID_bet'])
            
            #APOSTA REAL
            # print("**************",obj_cache_.stop_loss,"**************")
            if obj_cache_.list_bets_sinals: #and not obj_cache_.stop_loss:   
                tasks = []
                for item in obj_cache_.list_bets_sinals:
                    # if item.score_bet >= get_config.score and item.source == 'virtual_score' :
                    #     tasks.append(asyncio.create_task(aio_lib.play_bet(item)))
                    tasks.append(asyncio.create_task(aio_lib.play_bet(item)))
                    await asyncio.gather(*tasks)
            # task_status_waiting = asyncio.create_task(coroutine_task_status_waiting(message_status))
            # asyncio.gather(task_status_waiting)
    else:
        if obj_cache_id.ID_bet == message_status['ID_bet']:
            print("rodada válida")
        else:
            print("nao rodada válida")
               
        print('+++++RESULTADO: %s' % (message_status))
        if obj_cache_.list_bets_sinals: 
            obj_cache_.verify_win(message_status)

            #print("***********",obj_cache_.list_bets_sinals.vars())
            task_bets_sinals = asyncio.create_task(aio_lib.save_list_obj(obj_cache_.list_bets_sinals,'bets'))
            await asyncio.gather(task_bets_sinals)
            
            obj_cache_.list_bets_sinals.clear()
            obj_cache_.ajust_gale_()
            obj_cache_.list_bets_sinals = obj_cache_.list_gale_.copy()
            obj_cache_.list_gale_.clear()
            #obj_cache_.obj_balanceWin.stop_win()

        #print("==========balance==================")
        #print(obj_cache_.balanceWinDict)
        print("====================FIM==================================")  
            # task_status_rolling = asyncio.create_task(coroutine_task_status_rolling(message_status))
            # asyncio.gather(task_status_rolling)



async def coroutine_task_status_waiting(message_status):
    print("====================INICIO==================================")
    print('+++++PRONTO PARA APOSTAR: %s' % (message_status))
    #await asyncio.sleep(get_config.process_time)
    #time.sleep(10)
    await asyncio.sleep(3)
    print("FIM DA ESPERA DE:",3)
    
    #obj_cache_.convert_sinal_list_to_bet(message_status)
    obj_cache_.convert_sinal_to_bet(message_status)

    if obj_cache_.list_bets_sinals:
        #obj_cache_.score_bet()
        #obj_cache_.convert_score_bet(message_status)
        #print("ID_bet",message_status['ID_bet'])
        obj_cache_.set_id(message_status['ID_bet'])
        
        #APOSTA REAL
        # print("**************",obj_cache_.stop_loss,"**************")
        if obj_cache_.list_bets_sinals: #and not obj_cache_.stop_loss:   
            tasks = []
            for item in obj_cache_.list_bets_sinals:
                # if item.score_bet >= get_config.score and item.source == 'virtual_score' :
                #     tasks.append(asyncio.create_task(aio_lib.play_bet(item)))
                tasks.append(asyncio.create_task(aio_lib.play_bet(item)))
                await asyncio.gather(*tasks)
    
async def coroutine_task_status_rolling(message_status):
    # if obj_cache_id == message_status['ID_bet']:
    #     print("RODADA VÁLIDA",obj_cache_id,message_status['ID_bet'])
    # else:
    #     print("NOT RODADA VÁLIDA",obj_cache_id,message_status['ID_bet'])
    
    print('+++++RESULTADO: %s' % (message_status))
    if obj_cache_.list_bets_sinals: 
        obj_cache_.verify_win(message_status)

        #print("***********",obj_cache_.list_bets_sinals.vars())
        task_bets_sinals = asyncio.create_task(aio_lib.save_list_obj(obj_cache_.list_bets_sinals,'bets'))
        await asyncio.gather(task_bets_sinals)
        
        obj_cache_.list_bets_sinals.clear()
        obj_cache_.ajust_gale_()
        obj_cache_.list_bets_sinals = obj_cache_.list_gale_.copy()
        obj_cache_.list_gale_.clear()
        #obj_cache_.obj_balanceWin.stop_win()

    #print("==========balance==================")
    #print(obj_cache_.balanceWinDict)
    print("====================FIM==================================")   

            
class EchoServerProtocol_status:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message_status = json.loads(data.decode("utf-8"))
        message_status.update({'ajust_created_at': util.timestemp_to_string(message_status['timestamp'])})
        
        task_status_status = asyncio.create_task(coroutine_task_status_status(message_status))
        asyncio.gather(task_status_status)
        
        

        
            
class EchoServerProtocol_sinals:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message_signal = json.loads(data.decode("utf-8"))

        if not message_signal['type'] == 'list':
            obj_cache_.list_sinals.append(message_signal)
            print("----------",message_signal)
        else:
            #print("vai")
            #print(obj_cache_.dict_sinals)
            obj_cache_.dict_sinals.update({message_signal.get('source'): { 'sinals':message_signal.get('sinals')}})
            #print(obj_cache_.dict_sinals)

loop = asyncio.get_event_loop()
loop_signal = asyncio.get_event_loop()

# One protocol instance will be created to serve all client requests
obj_cache_ = cache_async()
obj_cache_id = ValidBet()
#obj_cache_async = cache_async

listen = loop.create_datagram_endpoint(   
    EchoServerProtocol_status, local_addr=('127.0.0.1', 20001))#PORTA STATUS DO SERVER NUVEM
listen_sinals = loop.create_datagram_endpoint(
    EchoServerProtocol_sinals, local_addr=('127.0.0.1', 20002)) #PORTA SINAIS

transport, protocol = loop.run_until_complete(listen)
transport_sinals, protocol = loop.run_until_complete(listen_sinals)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
transport_sinals.close()
transport.close()
loop.close()
