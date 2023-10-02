# importing modules
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# in case punkt needs to be donwloaded - it is necessary for stemming 
import nltk
nltk.download('punkt')
    
def deduceWordRoot(line): 
    ps = PorterStemmer()
    words = word_tokenize(line)
    
    newLine = ''
    
    for w in words:
        #print(w, " : ", ps.stem(w))
        line = line + ' ' + ps.stem(w)
        
    return newLine