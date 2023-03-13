
from api import get_config
import json
from api import util
class create_bet:
    def __init__(self, id, color, source,score_bet,created_ajust)-> None:
        self.id = id
        self.first_id_gale = id
        self.color = color
        self.source = source
        self.amount = get_config.amount
        self.score_bet = score_bet
        self.amount_return = 0
        self.gale = 0
        self.status_bet = None
        self.win = None
        self.win_status = None
        self.result_color = None
        self.created_ajust = created_ajust
    #def set_id_(self,id):
    #     self.id = id

class balanceWin():
    def calc_balance_win_bet(self, win,amount,color):
        if win:
            if color != 0:   
                win_bet = (amount/get_config.amount)
            else:
                win_bet = (amount * get_config.fator_branco)/get_config.amount - (amount / get_config.amount)
        else:
            if color != 0:   
                win_bet = -(amount/get_config.amount)
            else:
                win_bet =  -(amount/get_config.amount)
        return win_bet
                                                  
    # def stop_win(self):
    #     #print("===================stop==============")
    #     if self.win_Total >= get_config.stop_win:
    #         self.real_stop = True
    #     #print("===================True==============")

    # def stop_loss(self):
    #     #print("===================stop==============")
    #     if self.win_Total >= get_config.stop_loss:
    #         self.real_stop = True
    #     #print("===================True==============")
        
class balanceWinSource():
    def __init__(self) -> None:
        self.win = None

    def CalcBalanceWinSource(self,win, gale, source):
        print("")



class cache_async(create_bet,balanceWin):
    def __init__(self):  
        self.stop_loss = False
        self.list_sinals = []
        self.list_bets_sinals = []
        self.list_gale_ = []
        self.list_bets_sinals_score = []
        self.balanceWinDict = {}
        self.dict_gale = {'virtual_score': 2,
                          'bot': get_config.gale_limit,
                          'professor': get_config.gale_limit,
                          'aglair': 3,
                          'vip24hrs': get_config.gale_limit,                    
                          'trovaovip': get_config.gale_limit,
                          'robodouble': get_config.gale_limit,
                          'doubleimperial': get_config.gale_limit,  
                          'blazeoficial': get_config.gale_limit,
                          'brancoofical': 7,
                          'quebrancoablaze': get_config.gale_limit,
                          }
        self.dict_sinals = {}
        print("value",self.dict_gale)

    def convert_sinal_list_to_bet(self,message_status):
        #print("convert",self.dict_sinals)
        
        for item in list(self.dict_sinals.keys()):
            #print("item:",item)
            #print("item:",self.dict_sinals)
            #print(item,dicio.get(item).get('sinals').get('08:30'))
            print("***************",util.timestemp_to_string_H_M(message_status["created_at"]))
            item_aux = self.dict_sinals.get(item).get('sinals').get(util.timestemp_to_string_H_M(message_status["created_at"]))
            if item_aux:
                print(item_aux) 
                self.list_bets_sinals.append(create_bet(message_status['id'], 
                                                    item_aux['color'], item, 0,message_status['ajust_created_at']))   
                #print("bet",self.list_bets_sinals)
                print("pop:",self.dict_sinals.get(item).get('sinals').pop(util.timestemp_to_string_H_M(message_status["created_at"])))

        #print("fim:",self.dict_sinals)

    def convert_sinal_to_bet(self,message_status):
        if self.list_sinals:
            for item in self.list_sinals:
                if (item['time'] - message_status['created_at']) <= 5 and (item['time'] - message_status['created_at']) >= -15:
                    print(item['source'],"---------Diferença dentro" ,item['time'] - message_status['created_at'])
                    # color = item['color']
                    # if item['color'] == 1:
                    #     color = 2
                    # elif item['color'] == 2:
                    #     color = 1
                    # elif item['color'] == 0:
                    #     color = 0

                    # if self.balanceWinDict.get(item['source']):
                    #     if self.balanceWinDict.get(item['source']).get('win') > 0 :
                    #         if item['color'] == 1:
                    #             color = 2
                    #         elif item['color'] == 2:
                    #             color = 1
                    #     else:
                    #         color = item['color']
                    # else:
                    color = item['color']
                    
                    self.list_bets_sinals.append(create_bet(message_status['id'], 
                                                    color, item['source'], 0,message_status['ajust_created_at']))   

                else:
                    print(item['source']," ---------########Diferença fora #######--------" ,item['time'] - message_status['created_at'],)
            self.list_sinals.clear()
    
    def set_id(self,id):
        if self.list_bets_sinals:
            for item in self.list_bets_sinals:
                item.id = id
                
    def verify_win(self,message_status):
        for item in self.list_bets_sinals:
            if item.color == message_status['color'] and item.id == message_status['id']:
                item.win = balanceWin().calc_balance_win_bet(True,item.amount,item.color)
                item.win_status = 1
                item.result_color = message_status['color']
                item.amount_return = item.amount * 2
                if item.color == 0:
                    if item.gale < self.dict_gale.get(item.source):
                        self.list_gale_.append(item)

            else:
                print("---------------gale------------")
                item.win = balanceWin().calc_balance_win_bet(False,item.amount,item.color)
                item.win_status = -1
                item.result_color = message_status['color']

                print(item.source)
                if self.dict_gale.get(item.source):
                    print(self.dict_gale)
                    print(self.dict_gale.get(item.source), item.source)
                    if item.gale < self.dict_gale.get(item.source):
                        self.list_gale_.append(item)
                else:
                    if item.gale < get_config.gale_limit:
                        self.list_gale_.append(item)
                # if item.gale < get_config.gale_limit:
                #     self.list_gale_.append(item)

            if item.status_bet == 'created':
                source = 'real_bet'
                if  self.balanceWinDict.get(source):
                    self.balanceWinDict[source]['ajust_created_at'] = message_status['ajust_created_at']
                    self.balanceWinDict[source]['win'] += item.win
                    if 'G'+str(item.gale) in self.balanceWinDict.get(source):
                        self.balanceWinDict[source]['G'+str(item.gale)] += item.win
                    else:
                        self.balanceWinDict[source]['G'+str(item.gale)] = item.win
                else:
                    self.balanceWinDict.update({source:{'ajust_created_at' : message_status['ajust_created_at'] ,'source': source, 
                                                        'win' : item.win, 'G'+str(item.gale) : item.win}})
                    #0 <= -5 == False
                if (self.balanceWinDict.get(source).get('win') <= get_config.stop_loss) or (self.balanceWinDict.get(source).get('win') >= get_config.stop_win):
                    self.stop_loss = True
            

            
            source = item.source
            if  self.balanceWinDict.get(source):
                self.balanceWinDict[source]['ajust_created_at'] = message_status['ajust_created_at']
                self.balanceWinDict[source]['win'] += item.win
                if 'G'+str(item.gale) in self.balanceWinDict.get(source):
                    self.balanceWinDict[source]['G'+str(item.gale)] += item.win
                else:
                    self.balanceWinDict[source]['G'+str(item.gale)] = item.win
            else:
                self.balanceWinDict.update({source:{'ajust_created_at' : message_status['ajust_created_at'] ,'source': source, 
                                                    'win' : item.win, 'G'+str(item.gale) : item.win}})
                #0 <= -5 == False
            if (self.balanceWinDict.get(source).get('win') <= get_config.stop_loss) or (self.balanceWinDict.get(source).get('win') >= get_config.stop_win):
                self.stop_loss = True

            
            # if item.color == 0:
            #     win_status_ = item.win
            # else:
            #     win_status_ = item.win_status

            # if  self.balanceWinDict.get(item.source) and not (item.source == 'real_bet'):
            #     self.balanceWinDict[item.source]['ajust_created_at'] = message_status['ajust_created_at']
            #     self.balanceWinDict[item.source]['win'] += win_status_
            #     if 'G'+str(item.gale) in self.balanceWinDict.get(item.source):
            #         self.balanceWinDict[item.source]['G'+str(item.gale)] += win_status_
            #     else:
            #         self.balanceWinDict[item.source]['G'+str(item.gale)] = win_status_
            # elif not (item.source == 'real_bet'):
            #     self.balanceWinDict.update({item.source:{'ajust_created_at' : message_status['ajust_created_at'],'source': item.source, 
            #                                             'win' : win_status_, 'G'+str(item.gale) : win_status_}})


    def ajust_gale_(self):
        for item in self.list_gale_:
            item.gale += 1
            if item.color != 0:
                item.amount = item.amount * 2
                

    # def func_balance(self):
    #     for item in self.list_bets_sinals:              
    #         self.balanceWinDict.update({item.source:{'win_PV': item.win,'win_B':'','win_total': '' }})
    #     print("++++++++++++++func_balance:",self.balanceWinDict) 
        
          
    def score_bet(self):
        self.obj_score = class_score_bet()
        for item in self.list_bets_sinals:
            if  item.source != 'virtual_score':
                self.obj_score.calc_score(item.gale,item.color)
        self.obj_score.select_color()
        self.obj_score.action_real_bet()
        self.obj_score.score_print()
    
    def convert_score_bet(self,message_status):
        if self.obj_score.permission and not self.find_element_list('virtual_score'):
            self.list_bets_sinals.append(create_bet(message_status['id'], self.obj_score.decisao_color , 
                                                    self.obj_score.source, self.obj_score.total_score, message_status['ajust_created_at'] ))
        
        
    def find_element_list(self,value):
        for x in self.list_bets_sinals:
            if x.source == value:
                print("i found it!")
                return True
        else:
            print("i not found it!")
            return False
        
     
class class_score_bet():
    def __init__(self):
        self.total_score_c1 = 0
        self.total_score_c2 = 0
        self.decisao_color = None
        self.total_score = None
        self.permission = False
        self.source = 'virtual_score'

    def calc_score(self,gale,color):
        if color == 1:
            self.total_score_c1 += 1
        elif color == 2:
            self.total_score_c2 += 1
            
    def select_color(self):
        if self.total_score_c1 == self.total_score_c2:
            self.decisao_color = None
            self.total_score = 0    
        if self.total_score_c1 > self.total_score_c2:
            self.decisao_color = 1
            self.total_score = self.total_score_c1
        elif self.total_score_c2 > self.total_score_c1:
            self.decisao_color = 2
            self.total_score = self.total_score_c2
   
    def action_real_bet(self):
        if self.total_score >= get_config.score:
            self.permission = True
            
    def score_print(self):
        print("===================score_print==============")
        print("total_score_c1:",self.total_score_c1,
        "total_score_c2:",self.total_score_c2,
        "decisao_color:",self.decisao_color,
        "total_score:",self.total_score,
        "permission:",self.permission
        )
        print("===================score_print==============")
    def add_real_bet(self):
        if self.permission:
            print("class_create_bet")
               
                
