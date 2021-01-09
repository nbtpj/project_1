from biobert_embedding.embedding import BiobertEmbedding
from nltk import tokenize
from nltk.stem.porter import *
from nltk.corpus import stopwords
import os
from stanfordcorenlp import StanfordCoreNLP

LINK_TO_CORE_NLP = r'C:\Users\Nguyen Minh Quang\Desktop\DS_lab\project_1\corenlp'


def get_core_nlp():
    os.chdir(LINK_TO_CORE_NLP)
    os.system('java -mx8g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 5000')
    return StanfordCoreNLP('http://localhost', port=9000)


# open these lines if you run code first time
# nltk.download('stopwords')


class Sentence:
    BERT = BiobertEmbedding()
    STEMMER = PorterStemmer()
    STOPWORD = stopwords.words('english')
    NLP = StanfordCoreNLP(path_or_host=LINK_TO_CORE_NLP, memory='4g')

    def __init__(self, text='',
                 bert=BERT, json=None, nlp=NLP):
        self.nlp = nlp
        self.bert = bert
        self.n_of_nouns = 0
        self.n_of_numerals = 0
        self.pos_in_para = None
        self.tf_isf = None
        if json is None:
            temp_text = self.nlp.word_tokenize(text)
            self.tokens = [self.STEMMER.stem(word) for word in temp_text if word.lower() not in self.STOPWORD]
            temp_text = ' '.join(self.tokens)
            self.word_vector = bert.word_vector(temp_text)
            self.sentence_vector = bert.sentence_vector(temp_text)
            self.text = text
        else:
            self.word_vector = json["word_vec"]
            self.sentence_vector = json["vector"]
            temp_text = self.nlp.word_tokenize(json["text"])
            self.tokens = [self.STEMMER.stem(word) for word in temp_text if word.lower() not in self.STOPWORD]
            self.text = json["text"]

        for word, tag in self.pos_tag():
            if tag[0] is 'N':
                self.n_of_nouns += 1
            if tag is 'CD':
                self.n_of_numerals += 1

    def __str__(self):
        return self.text

    def pos_tag(self):
        """Part of speech tag"""
        return self.nlp.pos_tag(self.__str__())

    def constituency_parsing(self):
        """Constituency Parsing"""
        return self.nlp.parse(self.text)

    def dependency_parsing(self):
        """Dependency Parsing"""
        return self.nlp.dependency_parse(self.text)

    def ner(self):
        """Named-entity recognition"""
        return self.nlp.ner(self.text)

    def __abs__(self):
        """
        :return: a list of tensors:
           ___________________768 dimensions__________________________
        [ tensor([ 1.0497e+00, -6.3529e-01, ....  , -2.0922e+00]),    |
          tensor([ 1.0497e+00, -6.3529e-01, ....  , -2.0922e+00]),    |
          .                                                           number of words in the sentence
          .                                                           |
          .                                                           |
        ]

        """
        return self.word_vector

    def to_json(self):
        """
        :return:  an json-like format that can be dumped
        """
        return {
            "text": self.text,
            "word_vec": [d.tolist() for d in self.word_vector],
            "vector": self.sentence_vector.tolist()
        }

    def __len__(self):
        return len(self.tokens)


class Question(Sentence):
    pass


class Paragrapth:
    def __init__(self, text="", json=None):
        self.tokens = []
        self.sentences = []
        if json is None:
            for sen in tokenize.sent_tokenize(text):
                S = Sentence(text=sen)
                self.sentences.append(S)
                self.tokens.extend(S.tokens)
        else:
            for j in json:
                S = Sentence(json=json[j])
                self.sentences.append(S)
                self.tokens.extend(S.tokens)
        self.iter = 0

    def __next__(self):
        try:
            result = self.sentences[self.iter]
            self.iter += 1
            return result
        except:
            raise StopIteration

    def __add__(self, sent_para):
        """increase the current paragraph by adding with a sentence of paragraph"""
        if isinstance(sent_para, Sentence):
            self.sentences.append(sent_para)
        else:
            if isinstance(sent_para, Paragrapth):
                for sen in sent_para.sentences:
                    self.sentences.append(sen)
            else:
                raise TypeError(sent_para.__class__.__name__ + " can not be added with a Paragraph")
        self.tokens.extend(sent_para.tokens)
        return self

    def __str__(self):
        return ' '.join([str(sentence) for sentence in self.sentences])

    def __abs__(self):
        return [sentence.sentence_vector.tolist() for sentence in self.sentences]

    def to_json(self):
        return [sent.to_json() for sent in self.sentences]

    def __getitem__(self, key):
        return self.sentences[key]

    def __len__(self):
        return len(self.sentences)


class Entry:
    """A copy of raw data, has been processed (create new vectors)"""

    def __init__(self, json):
        self.question = Paragrapth(json["question"])
        self.multi_abs_summ = Paragrapth(json["multi_abs_summ"])
        self.multi_ext_summ = Paragrapth(json["multi_ext_summ"])
        self.answers = [
            {"answer_abs_summ": Paragrapth(json["answers"][item]["answer_abs_summ"]),
             "answer_ext_summ": Paragrapth(json["answers"][item]["answer_ext_summ"]),
             "article": Paragrapth(json["answers"][item]["article"]),
             "rating": json["answers"][item]["rating"]
             } for item in json["answers"]
        ]

    def to_json(self):
        """ :return: a json-like format that can be dumped
        {
            "question": __paragraph__
            "multi_abs_summ": __paragraph__
            "multi_ext_summ": __paragraph__
            "answers": [
                {
                    "answer_abs_summ": __paragraph__
                    "answer_ext_summ": __paragraph__
                    "article": __paragraph__
                    "rating": __text__
                }
            ]
        }
        """
        return {
            "question": self.question.to_json(),
            "multi_abs_summ": self.multi_abs_summ.to_json(),
            "multi_ext_summ": self.multi_ext_summ.to_json(),
            "answers":
                [
                    {"answer_abs_summ": item["answer_abs_summ"].to_json(),
                     "answer_ext_summ": item["answer_ext_summ"].to_json(),
                     "article": item["article"].to_json(),
                     "rating": item["rating"]
                     } for item in self.answers
                ]
        }


def if_isf():
    ...
