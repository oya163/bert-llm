import logging
from transformers import pipeline


LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def handle(event, context):
    if event.get("source") == "KEEP_LAMBDA_WARM":
        LOGGER.info("No ML work to do. Just staying warm...")
        return "Keeping Lambda warm"

    token_classifier = pipeline(
        "token-classification", model='./model/xlm-roberta-large', aggregation_strategy="simple"
    )
    results = token_classifier(text=event["text"])
    ret_val = {}
    for each_entity in results:
        ret_val[each_entity['word']] = each_entity['entity_group']
    return ret_val
