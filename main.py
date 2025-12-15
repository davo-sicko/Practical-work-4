import csv
import json

animals = [
    ['Животное', 'Среда обитания'],
    ['Медведь', 'Лес',],
    ['Дельфин', 'Океан',],
    ['Верблюд', 'Пустыня',]
]

file_path = 'C:/Users/david/OneDrive/Рабочий стол/All courses/2 Course/Python (НОВЫЙ)/Practical works/Practical work 4/animals.csv'

with open(file_path, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(animals)
 
headers = animals[0]





zoo_list = [
    dict(zip(headers, row))
    for row in animals[1:] 
]

file_path2 = 'C:/Users/david/OneDrive/Рабочий стол/All courses/2 Course/Python (НОВЫЙ)/Practical works/Practical work 4/zoo.json'

with open(file_path2, 'w', encoding='utf-8') as f:
    json.dump(zoo_list, f, ensure_ascii=False, indent=4)


file_path3 = 'C:/Users/david/OneDrive/Рабочий стол/All courses/2 Course/Python (НОВЫЙ)/Practical works/Practical work 4/csv_file.csv'
try:
    with open(file_path3, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            name = row['Имя'].strip()
            age_str = row['Возраст'].strip()
            try:
                age = int(age_str)
                if age > 30:
                    print(name)
            except (ValueError, TypeError):
                continue
except FileNotFoundError:
    print("Файл не найден")
    
    
def convert_csv_to_json(csv_path: str, json_path: str) -> None:
    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)
    
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

def convert_json_to_csv(json_path: str, csv_path: str) -> None:
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    if not data:
        return
    
    headers = data[0].keys()
    
    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
