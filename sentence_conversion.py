# Importing Required libraries

import spacy  # Spacy for text preprocessing
import pyinflect  # A python module for word inflections that works as a spaCy extension.

# Load small english model
nlp = spacy.load("en_core_web_sm")

# Parse text through the 'nlp' model
text = "The man asks what I am doing there."
doc = nlp(text)

def past_tensifier(doc, text):
    '''
    function to convert any type of sentence into past tense sentence.
    '''
    for i in range(len(doc)):
        token = doc[i]
        if token.tag_ in ['VBP', 'VBZ']:
            text = text.replace(token.text, token._.inflect("VBD"))
    return text


if __name__ == '__main__':
    past_sentence = past_tensifier(doc, text)
    print(past_sentence)
