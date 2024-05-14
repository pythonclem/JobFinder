from langdetect import detect

def is_english(text):
    if detect(text) == 'en':
        print("English")
    else:
        print("NOT English")

is_english("About the job Ben jij een behulpzame IT-liefhebber met een talent voor het oplossen van uitdagingen? Blink je uit in het moeiteloos oplossen van verschillende IT-gerelateerde vraagstukken? Dan verwelkomen wij jou graag als onze nieuwe IT Support Specialist!")