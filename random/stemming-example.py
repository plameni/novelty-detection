# importing modules
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# in case punkt needs to be donwloaded - it is necessary for stemming 
import nltk
nltk.download('punkt')
    
def main(): 
    ps = PorterStemmer()
      
    sentence = "Programmers program with programming languages"
    words = word_tokenize(sentence)
      
    for w in words:
        print(w, " : ", ps.stem(w))
    
main()