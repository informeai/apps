import re
from ast import literal_eval
import json
class JsonToCsv:
    
    def __init__(self, arquive:str):
        self.arquive = arquive

        with open(self.arquive, 'r') as arq:
            self.data = arq.read().replace('\n','').replace(' ','').replace('[','').replace(']','')
            arq.close()


    def extract_head(self):
        range_head = (str(self.data).index('{'), str(self.data).index('}'))
        head_initial = int(range_head[0])
        head_final = int(range_head[1])
        head = self.data[head_initial:head_final + 1]
        key_head = head.strip('{').strip('}').split(',')
        self.keys = [k[1: k.index(':') -1] for k in key_head]
        
        return self.keys

    def extract_body(self):
       
        body = self.data.split(',')
        self.val_body = [v.strip('{').strip('}').replace('"','') for v in body]
        return self.val_body
        