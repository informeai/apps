

class CsvToJson:
    
    def __init__(self, arquive:str, sep:str=','):
        self.arquive = arquive
        self.sep = sep

        with open(self.arquive, 'r') as arq:
            self.data = arq.readlines()
            arq.close()

        

    