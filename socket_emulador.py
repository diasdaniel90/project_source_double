
import json
from time import sleep
from api import util
from datetime import datetime

sleep(0.5)
timestamp_status = datetime.timestamp(datetime.now())
waiting_dict = json.dumps({'ID_bet': timestamp_status, 'timestamp': timestamp_status, 'bet_status': 'waiting'})
print(waiting_dict)
util.send_cliente(waiting_dict)

sleep(1)
timestamp = datetime.timestamp(datetime.now())
message_sinal = json.dumps({"type": "real_time", 'time': timestamp, 'color': 1, 'source': 'channel_1'})
print(message_sinal)
util.send_cliente_sinals(message_sinal)

sleep(1.2)
rolling_dict = json.dumps({'ID_bet': timestamp_status, 'timestamp': timestamp_status, 'bet_status': 'rolling', 'bet_color': 2, 'bet_roll': 13})
print(rolling_dict)
util.send_cliente(rolling_dict)



sleep(1.5)
timestamp_status = datetime.timestamp(datetime.now())
waiting_dict = json.dumps({'ID_bet': timestamp_status, 'timestamp': timestamp_status, 'bet_status': 'waiting'})
print(waiting_dict)
util.send_cliente(waiting_dict)

sleep(1)
rolling_dict = json.dumps({'ID_bet': timestamp_status, 'timestamp': timestamp_status, 'bet_status': 'rolling', 'bet_color': 1, 'bet_roll': 13})
print(rolling_dict)
util.send_cliente(rolling_dict)

sleep(1.5)
timestamp_status = datetime.timestamp(datetime.now())
waiting_dict = json.dumps({'ID_bet': timestamp_status, 'timestamp': timestamp_status, 'bet_status': 'waiting'})
print(waiting_dict)
util.send_cliente(waiting_dict)

sleep(1)
rolling_dict = json.dumps({'ID_bet': timestamp_status, 'timestamp': timestamp_status, 'bet_status': 'rolling', 'bet_color': 2, 'bet_roll': 13})
print(rolling_dict)
util.send_cliente(rolling_dict)

sleep(1.5)
timestamp_status = datetime.timestamp(datetime.now())
waiting_dict = json.dumps({'ID_bet': timestamp_status, 'timestamp': timestamp_status, 'bet_status': 'waiting'})
print(waiting_dict)
util.send_cliente(waiting_dict)

sleep(1)
rolling_dict = json.dumps({'ID_bet': timestamp_status, 'timestamp': timestamp_status, 'bet_status': 'rolling', 'bet_color': 1, 'bet_roll': 13})
print(rolling_dict)
util.send_cliente(rolling_dict)