from csv_to_json import CsvToJson
from json_to_csv import JsonToCsv











if __name__ == '__main__':
    csv = JsonToCsv('dados.json')
    csv.convert()