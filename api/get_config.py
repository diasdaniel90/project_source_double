import configparser
import json
config = configparser.ConfigParser()
config.read("api/config-list.ini")

amount = float(config['BET']['amount'])
amount_white = float(config['BET']['amount_white'])
gale_limit = int(config['BET']['gale'])
stop_win = int(config['BET']['stop_win'])
stop_loss = int(config['BET']['stop_loss'])
score = int(config['BET']['score'])
fator_branco = int(config['BET']['fator_branco'])
wallet = int(config['BET']['wallet'])
process_time = float(config['BET']['process_time'])
janela_minima = int(config['BET']['janela_minima'])
janela_maxima = int(config['BET']['janela_maxima'])
header_api = json.loads(config['HEADER_API']['TODOS'])
