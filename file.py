# -*- coding: utf-8 -*-
import json
import csv

with open ("LAI.csv","r") as f:
    reader = csv.reader(f,delimiter = ';')
    next(reader)
    data = {"Perguntas":[]}
    
    for row in reader:
        
        data['Perguntas'].append({"Mensagem":row[3].replace('é', 'e').replace('º', 'o').replace('ú', 'u').replace('ç', 'c').replace('á', 'a').replace('ê', 'e').replace('ã', 'a').replace('ó', 'o').replace('Á', 'A').replace('í', 'i')})
             
with open ("list.json","w") as f:
    json.dump(data,f,indent=4)    

