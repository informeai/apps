class JsonToCsv:
    
    def __init__(self, arquive:str):
        self.arquive = arquive

        with open(self.arquive, 'r') as arq:
            self.data = arq.readlines()
            arq.close()

        print(self.data)