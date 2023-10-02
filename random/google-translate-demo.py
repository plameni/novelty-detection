import json
import requests

def main():
    f = open('./../api-keys.json')
    data = json.load(f)
    googleTranslateApiKey = data['google-translate-api-key']
    queryParams = { 'key': googleTranslateApiKey }
    data = { 'q':'Testni primjer', 'source':'sr', 'target':'en' }
    url = 'https://translation.googleapis.com/language/translate/v2'
    response = requests.post(url, params=queryParams, data=data)
    response = json.loads(response.text)
    translatedText = response['data']['translations'][0]['translatedText']
    print(translatedText)
    
main()