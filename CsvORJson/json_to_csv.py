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
        keys = [k[1: k.index(':') -1] for k in key_head]
        
        return keys

    def extract_body(self):
       
        body = self.data.split(',')
        val_body = [v.strip('{').strip('}').replace('"','') for v in body]
        return val_body
    
    def convert(self):
        self.keys = self.extract_head()
        self.body = self.extract_body()

        text = ''
        for k in self.keys:
            text += f'{k},'
        text = text[:-1] + '\n'
        
        body = ''
        cont = 0
        for b in self.body:
            cont += 1
            index_initial = b.index(':') + 1
            b = b[index_initial:]
            body += f'{b},'
            if cont % len(self.keys) == 0:
                body = body[:-1] + '\n'
        
        return text + body
        
    def save(self,path:str):
        arq = open(path,'w')
        text = self.convert()
        arq.write(text)
        arq.close()