import warnings
warnings.filterwarnings('ignore')
import pickle
from flask import Flask,render_template, request
import preprocessing as pr


# Loading vectorizer
with open(r"C:\sds\project\self_project\sentiment analysis of emotions\tfidf_vect.pickle", 'rb') as f:
    tfidf_vect = pickle.load(f)
    
# Loading model
with open(r"C:\sds\project\self_project\sentiment analysis of emotions\model.pickle",'rb') as f:
    rfc=pickle.load(f)
    

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_emotion():
    
    text=request.form['text']
    x=text
    x=pr.remove_digits(x)
    x=pr.remove_punctuation(x)
    x=pr.accented_fixing(x)
    x=pr.contraction_fixing(x)
    x=pr.normalization(x)
    x=pr.remove_stopwords(x)
    x=pr.lemmatization(x)
    
    x=tfidf_vect.transform([x]).A
    emotion_label= {0: 'sadness', 1: 'anger', 2: 'love', 3: 'surprise', 4: 'fear', 5: 'joy'}
    
    pred=int(rfc.predict(x))
    emotion=emotion_label[pred]
    
    return render_template('index.html', prediction=f"""text: {text}   |   emotion: {emotion}""")

if __name__ == '__main__':
    app.run()


