# Install
download corenlp:

    wget http://nlp.stanford.edu/software/stanford-corenlp-latest.zip
unzip the release:
```
unzip stanford-corenlp-latest.zip
```
install requirements:

    pip install -r requirements.txt
download stopwords:

    python
    >> import nltk
    >> nltk.download('stopwords')

# Description
+ folde DATA contains raw data
+ set the LINK_TO_CORE_NLP in base_type.py by your own path to ..\stanford-corenlp-latest\stanford-corenlp-4.2.0
+ more documents: link.txt
