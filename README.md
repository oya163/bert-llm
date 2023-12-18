# Applications of Large Language Models

I am using Hugging Face libraries to perform model fine-tuning, evaluation and inference for various downstream tasks like Question-Answering, Named Entity Recognition and Text Classification.

## [Medical QA](https://github.com/oya163/bert-llm/tree/master/MedicalQA)
It contains all the necessary data and notebooks to fine-tune Question Answering task using Large Language Model (LLM) on the medical transcription dataset.

## [CyberSecurityNER](https://github.com/oya163/bert-llm/tree/master/CyberSecurityNER)
It contains all the necessary data and notebooks to fine-tune Named Entity Recognition task using Large Language Model (LLM) on the cyber security dataset.

## [NepNER](https://github.com/oya163/bert-llm/tree/master/NepNER)
In-depth analysis on Named Entity Recognition in Nepali Language using various Large Language Models. In this project, LLM is trained to extract abusive terms (Profanity, Violence and General) from the given texts written in Nepal language. The Nepali dataset is taken from the comment section of Nepali News Youtube channels.

### Dataset Statistics
| Dataset           | Count |
| -----------       | ----------- |
| Train             | 2323 |
| Test              | 280 |
| Validation        | 330 |

### Sample sentence

| Entity           | Label |
| -----------       | ----------- |
| भालुनी | B-PROFANITY
| सावित्री | O
| कुकुरनी | B-PROFANITY
| मिले | O
| को | O
| रहेछ | O
| आजा | O
| प्रक्षया | O
| थाहा | O
| भयो | O
| निर्माल | O
| बहिनी | O
| लाई | O
| बलत्कार | B-VIOLENCE
| गर्न | O
| लगाउने | O
| यनि | O
| भलु | B-PROFANITY
| हरु | O
| रहेछ | O
| । | O

### Evaluation

#### Sakonii/distilbert-base-nepali

| Metric      | Score |
| ----------- | ----------- |
| test_precision | 24.08% |
| test_recall    | 29.61% |
| test_f1        | 26.56% |
| test_accuracy  | 84.48% |
 
#### xlm-roberta-large

| Metric      | Score |
| ----------- | ----------- |
| test_precision | 38.26% |
| test_recall    | 44.50% |
| test_f1        | 41.15% |
| test_accuracy  | 86.15% |

### Inference

Input sentence = `त्यो साला खाते जलेर मरे हुन्छ ।`

| Word              | Predictions   |
| ----------------  | ------------- |
| साला खाते           |  GENERAL       |
| जलेर मरे            |   VIOLENCE     |

### Deployment

## [NepSA](https://github.com/oya163/bert-llm/tree/master/NepSA)
It contains all the necessary data and notebooks to fine-tune Abusive Sentiment Analysis Task in Nepali Langauge using various Large Language Models (LLM).
