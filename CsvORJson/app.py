from csv_to_json import CsvToJson
from json_to_csv import JsonToCsv











if __name__ == '__main__':
    json = JsonToCsv('dados.json')
    body = json.extract_body()
    # body = json.extract_body()
    print(body)
    # print(body)