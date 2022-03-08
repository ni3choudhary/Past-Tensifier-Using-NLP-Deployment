# Importing Required libraries
from flask import Flask,render_template,request,url_for  # using flask for web development
import spacy  # Spacy for text preprocessing
import pyinflect  # A python module for word inflections that works as a spaCy extension.

# load past_tensifier function from sentence_conversion file
from sentence_conversion import past_tensifier

# create flask app 
app = Flask(__name__) 

# Load small english model
nlp = spacy.load("en_core_web_sm")

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        text = request.form['sentence']
        # Parse text through the 'nlp' model
        doc = nlp(text)
        # call the function
        past_sentence = past_tensifier(doc, text)
        return render_template('index.html',show_hidden=True, past_sentence=past_sentence)
    return render_template('index.html',past_sentence='')


if __name__ == '__main__':
    app.run(debug=True)