
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords



swl=stopwords.words('english')
swl.remove('no')
swl.remove('not')
swl.remove('nor')


def remove_stopwords(data):             # defining a function to remove stopwords in the text 
    return ' '.join([i for i in data.split() if i.lower() not in swl])      




def normalization(data):        # defining a funtions to normalize the data, that is converting text into lower case
    return data.lower()



from string import punctuation

def remove_punctuation(data):       # defining a funtion to remove funtuation in text
    return ''.join([i for i in data if i not in punctuation])




def remove_digits(data):            # defining a function to remove digits in the text
    y=''
    for i in data:
        if i.isdigit()==False:
            y=y+i
    return y




import contractions                 
def contraction_fixing(data):           # a function to fix the contractions in the text
    return contractions.fix(data)



nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
def lemmatization(data):                        # a function to lemmetize words in text, i.e converting words in their base form
    lemma=WordNetLemmatizer()
    return lemma.lemmatize(data)




from unidecode import unidecode                 # function to fix accented text
def accented_fixing(data):
    return unidecode(data)





from autocorrect import Speller

def auto_correction(data):              # function for autocorrection of words in text
    spell=Speller(lang='en')
    return spell(data)







