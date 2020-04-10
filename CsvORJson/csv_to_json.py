

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