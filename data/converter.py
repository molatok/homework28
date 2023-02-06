import csv
import json

files = ('ads.csv', 'categories.csv', 'users.csv', 'location.csv')
new_row = []

def convert(files):
    """проходим по всем файлам в списке, для каждого создаем свой список со словарями, сохраняем список в json,
    чистим список для следующего """
    for file in files:
        with open(file, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            for row in rows:
                if 'id' in row.keys():
                    pk = int(row['id'])
                    del row['id']
                    new_row.append({'model': "ads" + '.' + file.split(".")[0], 'pk': pk, "fields": row})
                else:
                    pk = int(row['Id'])
                    del row['Id']
                    new_row.append({'model': "ads" + '.' + file.split(".")[0], 'pk': pk, "fields": row})
                with open(file.split(".")[0] + '.json', 'w', encoding='utf-8') as f:
                    json.dump(new_row, f, ensure_ascii=False)
        new_row.clear()


convert(files)