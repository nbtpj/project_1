import os
from math import log, e, cos

import numpy as np
from biobert_embedding.embedding import BiobertEmbedding
from nltk.corpus import stopwords
from nltk.stem.porter import *
from stanfordcorenlp import StanfordCoreNLP

STOPWORD = stopwords.words('english')
LINK_TO_CORE_NLP = r'C:\Users\Nguyen Minh Quang\Desktop\DS_lab\project_1\corenlp'
TEST_RESULT = open('DATA/result.txt', mode='a+')


def tf(term, sen):
    """
    Term Frequency
    :param term: word
    :param sen: sentence
    :return: the importance of a term in a sentence by it's frequency
    """
    n = 0.0
    for word in sen:
        if term == word:
            n += 1.0
    return n / len(sen)


def isf(term, para):
    """
    Inverse Sentence Frequency
    :param term: word
    :param para: paragraph
    :return: the importance of term in paragraph
    """

    n = 0.0
    for sen in para:
        if term in sen.tokens:
            n += 1.0
    return log(len(para) / n, e)


def tf_isf(sen, para):
    """
    Term Frequency-Inverse Sentence Frequency
    :param sen: sentence
    :param para: paragraph
    :return: the importance of sentence in paragraph
    """
    s = 0
    for word in sen:
        s += tf(word, sen) * isf(word, para)
    return s / len(para)


def text_preprocess(text):
    text = text.strip().lower()
    rs = ""
    for word in text.split(' '):
        if word not in STOPWORD:
            rs += word
    return rs


def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)


def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def get_core_nlp():
    os.chdir(LINK_TO_CORE_NLP)
    os.system('java -mx8g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 5000')
    return StanfordCoreNLP('http://localhost', port=9000)


# open these lines if you run code first time
# nltk.download('stopwords')


class Sentence:
    """
    Sentence class:
        - save a raw text of the sentence (self.text)
        - preprocess:
            + tokenize          | => create | word     |vector
            + remove stop words |           | sentence |
            + lower             |           | self.tokens
                                | => extract features

    """
    BERT = BiobertEmbedding()
    STEMMER = PorterStemmer()

    NLP = StanfordCoreNLP(path_or_host=LINK_TO_CORE_NLP, memory='4g')

    def __init__(self, text='',
                 bert=BERT, json=None, nlp=NLP):
        self.iter = 0
        self.nlp = nlp
        self.similarity = None
        self.bert = bert
        self.n_of_nouns = 0
        self.n_of_numerals = 0
        self.pos_in_para = None
        self.tf_isf = None
        self.pos_tag_ = None
        if json is None:
            text = text.strip()
            self.text = text
            text = text_preprocess(text)
            self.word_vector = bert.word_vector(text)
            self.sentence_vector = bert.sentence_vector(text)
            self.tokens = bert.tokens
            for word, tag in self.pos_tag():
                if tag[0] is 'N':
                    self.n_of_nouns += 1
                if tag == 'CD':
                    self.n_of_numerals += 1
            self.n_of_numerals /= len(self)

        else:
            self.word_vector = json["word_vec"]
            self.sentence_vector = json["vector"]
            self.tokens = json["tokens"]
            self.text = json["text"]
            self.n_of_nouns = json["n_of_nouns"]
            self.n_of_numerals = json["n_of_numerals"]
            self.similarity = json["similarity"]
            self.pos_tag_ = json["pos_tag"]

        TEST_RESULT.write(self.info())

    def __str__(self):
        return self.text

    def __iter__(self):
        self.iter = 0
        return self

    def __next__(self):
        try:
            result = self.tokens[self.iter]
            self.iter += 1
            return result
        except:
            raise StopIteration

    def __getitem__(self, key):
        return self.tokens[key]

    def pos_tag(self):
        """Part of speech tag"""
        if self.pos_tag_ is None:
            self.pos_tag_ = self.nlp.pos_tag(self.text)
        return self.pos_tag_

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
            "vector": self.sentence_vector.tolist(),
            "n_of_nouns": self.n_of_nouns,
            "n_of_numerals": self.n_of_numerals,
            "similarity": self.similarity,
            "tokens": self.tokens,
            "pos_tag": self.pos_tag_
        }

    def __len__(self):
        return len(self.tokens)

    def info(self):
        return "{" + "\n\ttext: " + self.text + "\n\tpos_tag: " + str(
            self.pos_tag_) + "\n\tnumber of nouns: " + str(
            self.n_of_nouns) + "\n\tf_numerals: " + str(
            self.n_of_numerals) + "\n\ttf-isf: " + str(self.tf_isf) + "\n\tsimilarity: " + str(
            self.similarity) + "\n}\n"


class Question(Sentence):
    pass


class Paragrapth:
    def __init__(self, text="", js=None):
        print(text)
        self.tokens = []
        self.sentences = []
        if js is None:
            text = text.strip()
            out = text.split('. ')
            # out = Sentence.NLP.annotate(text=text, properties={
            #     'annotators': 'ssplit',
            #     'outputFormat': 'json'
            # })
            # print('done')
            # try:
            #     m = []
            #     out = json.loads(out)
            #     for sen in out['sentences']:
            #         m.append(' '.join([token['word'] for token in sen['tokens']]))
            #     out = m
            # except Exception as e:
            #     print(str(e))

            for sen in out:
                s = Sentence(text=sen)
                if len(s) > 2:
                    self.sentences.append(s)
                    self.tokens.extend(s.tokens)


        else:
            for j in js:
                s = Sentence(json=js[j])
                self.sentences.append(s)
                self.tokens.extend(s.tokens)
        self.iter = 0

    def __iter__(self):
        self.iter = 0
        return self

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

    def info(self):
        rs = str([sen.info() for sen in self])
        return rs

    def fill_sentence_feature(self, center_ques=None):
        for sen in self.sentences:
            sen.tf_isf = tf_isf(sen, self)
            if sen is self.sentences[0] or sen is self.sentences[len(self) - 1]:
                sen.pos_in_para = 1
            else:
                sen.pos_in_para = 0
            if center_ques is not None:
                sen.similarity = 0
                for sen_p in center_ques:
                    sen.similarity += cos(angle_between(sen_p.sentence_vector, sen.sentence_vector)) / len(center_ques)
        return self


class Entry:
    """A copy of raw data, has been processed (create new vectors)"""

    def __init__(self, json):
        self.question = Paragrapth(json["question"])
        self.multi_abs_summ = Paragrapth(json["multi_abs_summ"]).fill_sentence_feature(self.question)
        self.multi_ext_summ = Paragrapth(json["multi_ext_summ"]).fill_sentence_feature(self.question)
        self.answers = [
            {
                "answer_abs_summ": Paragrapth(text=json["answers"][item]["answer_abs_summ"]).fill_sentence_feature(
                    self.question),
                "answer_ext_summ": Paragrapth(text=json["answers"][item]["answer_ext_summ"]).fill_sentence_feature(
                    self.question),
                "article": Paragrapth(text=json["answers"][item]["article"]).fill_sentence_feature(self.question),
                "rating": json["answers"][item]["rating"]
            }
            for item in json["answers"]
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
