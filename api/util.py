from datetime import datetime, timezone, timedelta
import csv
import json
import http.client
import configparser
import socket
config = configparser.ConfigParser()
config.read("api/config-list.ini")
header_api = json.loads(config['HEADER_API']['TODOS'])

bufferSize          = 1024
# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

serverAddressPortSinals = ("127.0.0.1", 20002)#PORTA SINAIS
serverAddressPort_client   = ("127.0.0.1", 20001)#PORTA STATUS DO SERVER NUVEM

def send_cliente(msg):
    # Send to server using created UDP socket
    bytesToSend         = str.encode(msg)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort_client)


def send_cliente_sinals(msg):
    # Send to server using created UDP socket
    bytesToSend         = str.encode(msg)
    UDPClientSocket.sendto(bytesToSend, serverAddressPortSinals)

def play(color,amount):
    conn = http.client.HTTPSConnection("blaze.com")
    payload = '{"amount":"%s","currency_type":"BRL","color":%d,"free_bet":false,"wallet_id":48396129}' % (amount, color)
    conn.request("POST", "/api/roulette_bets", payload, header_api)
    res = conn.getresponse()
    data = res.read()
    json_ = json.loads(data.decode("utf-8"))
    if 'bet' in json_:
        return json_.get('bet')['status']
    if 'error' in json_:
        return json_.get('error')['code']
    #dicio.get('bet')['status'] create
    #json_['error']['code'] 1078 minimo
    #json_['error']['code'] 1040 nao é a hora de apostar
    #dicio.get('bet')['status'] create
    #json_['error']['code'] 1078 minimo
    #json_['error']['code'] 1040 nao é a hora de apostar
    
def on_open(ws):
    message = '%d["cmd", {"id": "subscribe", "payload": {"room": "double_v2"}}]' % 421
    ws.send(message)
    print("debug")

def on_pong(ws):
    ws.send("2")
    
    
# def last_doubles(result_dict):
#         return (dict({ 'id' : result_dict["id"],
#                         #'color': get_color(result_dict["color"]), 'roll': result_dict["roll"],
#                         'created_at': date_list(result_dict["created_at"]), #'updated_at':result_dict["updated_at"],
#                         'status': result_dict["status"], 'bet_time': timestemp_to_string(result_dict["created_at"]),
#                         }))

# def bet_last_doubles(result_dict, item, balance_win):
#     return (dict({ 'id' : result_dict["id"],
#                         'color': get_color(result_dict["color"]), 'roll': result_dict["roll"],
#                         'created_at': date_list(result_dict["created_at"]),# 'updated_at':result_dict["updated_at"],
#                         'status': result_dict["status"], 'bet_time': timestemp_to_string(result_dict["created_at"]),
#                         'status_bet':item.status_bet, 'win': item.win, 'gale': item.count_gale, 'first_gale': item.first_gale, 'amount':item.amount,
#                         'return_amount': item.return_amount, 'win_PV': balance_win.win_PV,'win_B': balance_win.win_B,'win_Total':balance_win.win_Total
#                         }))

# def report(save_):
#     #fieldnames = ['id', 'color', 'roll','created_at','bet_time','status_bet','win','gale', 'first_gale', 'amount','return_amount','win_PV','win_B','win_Total']
#     with open('report_result.csv', 'a') as f:
#         writer = csv.DictWriter(f, fieldnames=save_.keys())
#         #writer.writeheader()
#         print(save_)
#         writer.writerow(save_)

def get_color(number):
    colors = {
        0: "branco",
        1: "vermelho",
        2: "preto"
    }
    return colors.get(number, None)

def get_number(color):
    number = {
        'branco': 0,
        'vermelho': 1,
        'preto' : 2
    }
    return number.get(color, None)


def ajuste(date):
    date = str(date)
    #print("date:",date)
    # diferenca = timedelta(hours=-6)
    # fuso_horario = timezone(diferenca)
    date = datetime.strptime(date,"%Y-%m-%dT%H:%M:%S.%fZ") 
    return date - timedelta(hours=3)
    #return date.astimezone(fuso_horario)


def date_to_timestemp(date):
    #ajuste_ = ajuste(date)
    #print("ajust:",ajuste_)
    date = datetime.strptime(date,"%Y-%m-%dT%H:%M:%S.%fZ") 
    return datetime.timestamp(date)

def timestemp_to_string(timestemp_):
    return datetime.fromtimestamp(timestemp_).strftime("%Y-%m-%dT%H:%M:%S")

def timestemp_to_string_H_M(timestemp_):
    return datetime.fromtimestamp(timestemp_).strftime("%H:%M")

def date_list(date):
    return ajuste(date).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

def date_bet_H_M(date):
    return ajuste(date).strftime("%H:%M")



class Util:
    def __init__(self,date):
        print("init date")
        diferenca = timedelta(hours=-6)
        fuso_horario = timezone(diferenca)
        self.date = datetime.strptime(date,"%Y-%m-%dT%H:%M:%S.%fZ") 
        self.date = self.date.astimezone(fuso_horario)
       
    def get_date_ajust(self):
        return self.date.strftime("%Y-%m-%d|%H:%M:%S:%f")
        
    def get_date_list(self):
        return self.date.strftime("%H")
# strdate = '2022-09-11T06:07:45.913Z'
# print(Util(strdate).get_date_ajust())
# print(Util(strdate).get_date_list())

