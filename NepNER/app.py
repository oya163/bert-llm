from transformers import pipeline
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """Basic HTML response."""
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to Nepali NER</h1>"
        "</body>"
        "</html>"
    )
    return body

@app.route("/predict", methods=["POST"])
def predict():
    data_json = request.get_json()
    token_classifier = pipeline(
        "token-classification", model='./model/xlm-roberta-large', aggregation_strategy="simple"
    )
    results = token_classifier(data_json['sentence'])
    ret_val = {}
    for each_entity in results:
        ret_val[each_entity['word']] = each_entity['entity_group']
    return ret_val

if __name__ == "__main__":
    app.run()