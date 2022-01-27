import uvicorn
from fastapi import FastAPI
from Incoming import Query
import pandas as pd
import numpy as np
import spacy

app = FastAPI()
nlp = spacy.load("en_my_pipeline")

@app.get ("/")
def index():
    return {'message': 'Hello, Stranger'}

@app.post("/predict/")
def predict(data:Query):
    data = data.dict()
    print(data)
    print("Hello")
    text = data['text']
    print(text)
    texts = [text]
    docs = [nlp.tokenizer(text) for text in texts]
    textcat = nlp.get_pipe('textcat')
    scores = textcat.predict(docs)
    predicted_labels = scores.argmax(axis=1)
    result = [textcat.labels[label] for label in predicted_labels]
    print(result)
    return {
        'result': result[0]
    }

if __name__ == '__main__':
    uvicorn.run(app, host= '127.0.0.1', port= 8000)



