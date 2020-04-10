

class CsvToJson:
    
    def __init__(self, arquive:str, sep:str=','):
        self.arquive = arquive
        self.sep = sep

        with open(self.arquive, 'r') as arq:
            self.data = arq.readlines()
            arq.close()

        

    def extract_head(self):
        try:
            return self.data[0].strip('\n').split(self.sep)
           
        except Exception as e:
            print(e)
    def extract_body(self):
        try:
            return [b.strip('\n').split(self.sep) for b in self.data[1:]]

        except Exception as e:
            print(e)

    def valuate_number(self,value):
        try:
            v = int(value)
            return v
        except Exception:
            return f'"{value}"'
    
    def convert(self):
        self.head = self.extract_head()
        self.body = self.extract_body()
        text = '['
        for b in self.body:
            text += '{'
            for i in range(len(self.head)):

                text += f'"{self.head[i]}":{self.valuate_number(b[i][:])},'
                if i == len(self.head) -1:
                    text = text[:-1]
            text += '},'
        text = text[:-1] + ']'
        return text

    def save(self, path:str):
        arq = open(path, 'w')
        text = self.convert()
        arq.write(text)
        arq.close()