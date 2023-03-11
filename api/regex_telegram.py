# -*- coding: utf-8 -*-
import re
def channel_aglair(message):
    lines = re.sub(r"[^0-9🔴⚫️👻:\n ]","",message)
    dicio = {}
    teste = lines.split("\n")
    for item in teste:
        if re.search(':', item,re.IGNORECASE):
            #print(item[0:5]) #hora
            #print(item[5:6]) #color
            #print(item[8:9]) #branco
            if re.search('⚫️️', item,re.IGNORECASE):
                dicio.update({item[0:5]:{'hora': item[0:5], 'color':2 ,'branco': 0}})
            elif re.search('🔴', item,re.IGNORECASE):
                dicio.update({item[0:5]:{'hora': item[0:5],'color':1,'branco': 0}})
            if re.search('👻', item,re.IGNORECASE):
                #print(item)
                #dicio.update({item[0:5]:{'branco':True}})
                dicio[item[0:5]]['branco'] = 1
                #dicio = {**dicio, 'branco':True}
    return dicio

# print(read_dict())  
# print(read_dict())  

def channel_branco_ofical(message):
    lines = re.sub(r"[^0-9🔴⚫️👻:\n ]","",message)
    dicio = {}
    teste = lines.split("\n")
    for item in teste:
        if re.search(':', item,re.IGNORECASE):
            #print(item[0:5]) #hora
            #print(item[5:6]) #color
            #print(item[8:9]) #branco
            if re.search('⚫️️', item,re.IGNORECASE):
                dicio.update({item[0:5]:{'hora': item[0:5], 'color':2 ,'branco': 0}})
            elif re.search('🔴', item,re.IGNORECASE):
                dicio.update({item[0:5]:{'hora': item[0:5],'color':1,'branco': 0}})
            if re.search('👻', item,re.IGNORECASE):
                #print(item)
                #dicio.update({item[0:5]:{'branco':True}})
                dicio[item[0:5]]['branco'] = 1
                #dicio = {**dicio, 'branco':True}
    return dicio