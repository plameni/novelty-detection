from googletrans import Translator

def translate(line): 
    try:
        translator = Translator()
        result = translator.translate(line, dest='en', src='sr')
        return result.text
    except: 
        return False