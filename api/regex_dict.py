# -*- coding: utf-8 -*-
import re
def read_dict():
    with open("api/sample_list.txt","a") as f:
        lines = f.read()
        lines = re.sub(r"[^0-9🔴⚫️👻:\n ]","",lines)
        dicio2 = {}
        teste = lines.split("\n")
        for item in teste:
            if re.search(':', item,re.IGNORECASE):
                #print(item[0:5]) #hora
                #print(item[5:6]) #color
                #print(item[8:9]) #branco
                if re.search('⚫️️', item,re.IGNORECASE):
                    dicio2.update({item[0:5]:{'hora': item[0:5], 'color':'preto','branco':False}})
                elif re.search('🔴', item,re.IGNORECASE):
                    dicio2.update({item[0:5]:{'hora': item[0:5],'color':'vermelho','branco':False}})
                if re.search('👻', item,re.IGNORECASE):
                    #print(item)
                    #dicio2.update({item[0:5]:{'branco':True}})
                    dicio2[item[0:5]]['branco'] = True
                    #dicio2 = {**dicio2, 'branco':True}
    return dicio2

# print(read_dict())  
# print(read_dict())  

