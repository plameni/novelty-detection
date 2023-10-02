from googletrans import Translator 

def main():
    translator = Translator()
    #translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
    #for translation in translations:
    #    print(translation.origin, ' -> ', translation.text)
    
    translation = translator.translate('Testni primjer', dest='en', src='sr')
    print(translation)
    print(translation.text)
    
main()