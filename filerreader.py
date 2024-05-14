import datetime
import csv

def format_text(input_text):
    formatted_text = input_text.replace("''", "'")
    formatted_text = formatted_text.replace("\n", " ")
    formatted_text = formatted_text.strip()
    return formatted_text

def read_file():
        today = datetime.date.today()
        filename = f'{today}-jobs.csv'
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row[1]) > 100:
                    print(format_text(row[1]))



read_file()