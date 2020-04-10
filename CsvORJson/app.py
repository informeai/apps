from csv_to_json import CsvToJson
from json_to_csv import JsonToCsv











if __name__ == '__main__':
    csv = CsvToJson('dados.csv')
    head = csv.extract_head()
    body = csv.extract_body()
    print(head)
    print(body)