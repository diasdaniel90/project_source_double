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
        if result_dict["status"] == "waiting" and self.updated_at != result_dict["updated_at"]:
            self.updated_at = result_dict["updated_at"]
            print("PRONTO PARA APOSTAR")
            #print(result_dict)
            self.timestemp_waiting = util.date_to_timestemp(result_dict["created_at"])
            waiting_dict = {'ID_bet': result_dict['id'],'timestamp': self.timestemp_waiting,
                            'bet_roll': result_dict['roll'], 'bet_color': result_dict['color'],
                            'bet_status':result_dict['status']}
            print(waiting_dict)
            server_result = ServerResult.objects.create(**waiting_dict)
            server_result.save()
            
            #util.send_cliente(json.dumps(waiting_dict))             
            #self.bet_list(result_dict)
        elif result_dict["status"] == "rolling" and self.updated_at != result_dict["updated_at"]:
            self.updated_at = result_dict["updated_at"]
            print("APOSTAS FECHADAS")
            #print(result_dict)
            self.timestemp_rolling = util.date_to_timestemp(result_dict["created_at"])

            waiting_dict = {'ID_bet': result_dict['id'],'timestamp': self.timestemp_waiting,
                            'bet_roll': result_dict['roll'], 'bet_color': result_dict['color'],
                            'bet_status':result_dict['status']}
            try:
                server_result = ServerResult.objects.get(ID_bet=result_dict['id'])
                server_result.bet_color = result_dict['color']
                server_result.bet_roll = result_dict['roll']
                server_result.save()
            except ServerResult.DoesNotExist:
                print("objeto nao encontrado erro na comunicação com o server")
            
            print(waiting_dict)    
            #util.send_cliente(json.dumps(rolling_dict))
            #rolling_dict['ajust_created_at'] = util.timestemp_to_string(self.timestemp_rolling)
            #util.report(rolling_dict)
            

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