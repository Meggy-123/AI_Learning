def save_record(record, filename):
    with open(filename, 'a', encoding='utf-8') as file:

        file.write(f"{record['name']},{record['weight']},{record['height']},{record['bmi']},{record['category']}\n")