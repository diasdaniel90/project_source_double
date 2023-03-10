from multiprocessing.connection import wait
import websocket
import threading
from time import sleep
import json
import configparser
from datetime import datetime
from api import util
from api import regex_dict
from api.models import ServerResult

config = configparser.ConfigParser()
config.read("api/config-list.ini")
header_ws = json.loads(config['HEADER_WS']['TODOS'])
url_socket = config['BET']['url_socket']

#dict_channel = regex_dict.read_dict()

class ControlSend:   
    def __init__(self):
        self.updated_at = None

    def on_open(self,ws):
        #websocket.enableTrace(True)
        message = '%d["cmd", {"id": "subscribe", "payload": {"room": "double_v2"}}]' % 421
        ws.send(message)

    def on_pong(self,ws, msg):
        ws.send("2")

    def on_close(self,ws, status, msg):
        print("morreu")
        sleep(1)
        self.connect_websocket()
        
    def on_message(self,ws, msg):
        #print(msg)
        if "double.tick" in msg:
            result_dict = json.loads(msg[2:])[1]["payload"]
            self.teste_msg(result_dict)
            
    def teste_msg(self,result_dict):
        self.acumulativo_banca = 0
        if result_dict["status"] == "waiting" and self.updated_at != result_dict["updated_at"]:
            self.updated_at = result_dict["updated_at"]
            print("PRONTO PARA APOSTAR_")
            timestemp_ = util.date_to_timestemp(result_dict["created_at"])
            result_dict_ = {'ID_bet': result_dict['id'],
                            'timestamp': timestemp_,
                            'bet_status':result_dict['status']}
            print(result_dict_)
            server_result = ServerResult.objects.create(**result_dict_)
            server_result.save()
            
        elif result_dict["status"] == "rolling" and self.updated_at != result_dict["updated_at"]:
            self.updated_at = result_dict["updated_at"]
            print("APOSTAS FECHADAS_")
            timestemp_ = util.date_to_timestemp(result_dict["created_at"])
                        
            result_dict_ = {'ID_bet': result_dict['id'],'timestamp': timestemp_,
                            'bet_roll': result_dict['roll'], 'bet_color': result_dict['color'],
                            'bet_status' : result_dict['status'],
                            'total_red_eur_bet' : result_dict['total_red_eur_bet'],
                            'total_red_bets_placed' : result_dict['total_red_bets_placed'],
                            'total_white_eur_bet' : result_dict['total_white_eur_bet'],
                            'total_white_bets_placed' : result_dict['total_white_bets_placed'],
                            'total_black_eur_bet' : result_dict['total_black_eur_bet'],
                            'total_black_bets_placed' : result_dict['total_black_bets_placed'],
                            'total_bets_placed' : result_dict['total_red_bets_placed'] + result_dict['total_white_bets_placed'] + result_dict['total_black_bets_placed'],
                            'total_eur_bet' :  result_dict['total_white_eur_bet'] + result_dict['total_red_eur_bet'] + result_dict['total_black_eur_bet']
                            }
            if result_dict_['bet_color'] == 0:
                result_dict_['total_retention_eur'] = result_dict_['total_eur_bet']  - (result_dict['total_white_eur_bet'] * 14)
            elif result_dict_['bet_color'] == 1 :
                result_dict_['total_retention_eur'] = result_dict_['total_eur_bet']  - (result_dict['total_red_eur_bet'] * 2 )
                # print(type(result_dict['total_red_eur_bet']))
                # print((result_dict['total_red_eur_bet'] * 2))
                # print(result_dict_['total_eur_bet']  - result_dict['total_red_eur_bet'])
            else:
                result_dict_['total_retention_eur'] = result_dict_['total_eur_bet']  - (result_dict['total_black_eur_bet'] * 2)
                # print(type(result_dict['total_black_eur_bet']))
                # print((result_dict['total_black_eur_bet']*2))
                # print(result_dict_['total_eur_bet']  - result_dict['total_black_eur_bet'])
            print("TOTAL",result_dict_['total_eur_bet'] )
            print(result_dict_)
            self.acumulativo_banca += result_dict_['total_retention_eur']
            print("$$$$$$$",self.acumulativo_banca ,"$$$$$$$$$$")
              
            try:
                server_result = ServerResult.objects.get(ID_bet=result_dict_['ID_bet'])
                server_result.bet_color = result_dict_['bet_color']
                server_result.bet_roll = result_dict_['bet_roll']
                server_result.bet_status = result_dict_['bet_status']
                server_result.total_red_eur_bet = result_dict_['total_red_eur_bet']
                server_result.total_red_bets_placed = result_dict_['total_red_bets_placed']
                server_result.total_white_eur_bet = result_dict_['total_white_eur_bet']
                server_result.total_white_bets_placed = result_dict_['total_white_bets_placed']
                server_result.total_black_eur_bet = result_dict_['total_black_eur_bet']
                server_result.total_black_bets_placed = result_dict_['total_black_bets_placed']
                server_result.total_eur_bet = result_dict_['total_eur_bet']
                server_result.total_bets_placed = result_dict_['total_bets_placed']
                server_result.total_retention_eur = result_dict_['total_retention_eur']
         
                server_result.save()
            except ServerResult.DoesNotExist:
                server_result = ServerResult.objects.create(**result_dict_)
                server_result.save()
                print("objeto nao encontrado erro na comunicação com o server")            


            
            
    # função abaixo faz o tratamento de fonte de sinal por lista.
    # def bet_list(self,result_dict):  
    #     if (dict_channel.get(util.date_bet_H_M(result_dict["created_at"]))):
    #         message_sinal = json.dumps(dict_channel.get(util.date_bet_H_M(result_dict["created_at"])))
    #         util.send_cliente_sinals_sinals(message_sinal)
    #         print(dict_channel.get(util.date_bet_H_M(result_dict["created_at"])))
    #         #print("SINAL: ",dict_channel.pop(util.timestemp_to_string(result_dict["created_at"])))
            
    def connect_websocket(self):
        print(url_socket)
        ws = websocket.WebSocketApp("wss://api-v2.blaze.com/replication/?EIO=3&transport=websocket",
            header=header_ws,
            on_open=self.on_open,
            on_message=self.on_message,
            on_close=self.on_close,
            on_pong=self.on_pong
        )
        ws_run = ws.run_forever(ping_interval=23,
                        ping_timeout=15,
                        ping_payload="3",
                        origin="https://blaze.com",
                        host="api-v2.blaze.com")
        wst = threading.Thread(target=ws_run)
        wst.daemon = True
        wst.start()
        
def main():
    try:
        ControlSend().connect_websocket()
    except Exception as err:
        print(err)
        print("connect failed")
        
# if __name__ == '__main__':
#     main()
