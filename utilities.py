import csv
from langdetect import detect


def format_text(input_text):
    formatted_text = input_text.replace('"', "'")
    formatted_text = formatted_text.replace("\n", " ")
    formatted_text = formatted_text.strip()
    return formatted_text

def is_english(text):
    if detect(text) == 'en':
        return True
    else:
        return False
    
def create_file():
    try:
        filename = 'jobs.csv'
        with open(filename, 'x', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
    except FileExistsError:
        pass