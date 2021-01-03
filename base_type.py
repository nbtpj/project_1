from biobert_embedding.embedding import BiobertEmbedding
import nltk
from nltk import tokenize
# from nltk.corpus import state_union
# from nltk.tokenize import PunktSentenceTokenizer
# from nltk.corpus import treebank
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


# open these lines if you run code first time
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('conll2000')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# nltk.download('large_grammars')


class Rule:
    def match(self, sentence):
        raise NotImplementedError


class Sentence:
    #  Văn phạm
    GRAMMAR = nltk.data.load('grammars/large_grammars/atis.cfg')
    BERT = BiobertEmbedding()

    # khởi tạo với dữ liệu bert, text|json
    def __init__(self, text='',
                 bert=BERT, json=None):
        self.bert = bert
        if json is None:
            self.word_vector = bert.word_vector(text)
            self.sentence_vector = bert.sentence_vector(text)
            self.text = word_tokenize(text)
        else:
            self.word_vector = json["word_vec"]
            self.sentence_vector = json["vector"]
            self.text = word_tokenize(json["text"])

    def __str__(self):
        return ' '.join(self.text)

    # gán nhãn cho mỗi từ
    def tag(self):
        return pos_tag(self.text)

    def chunking(self):
        return nltk.ne_chunk(self.tag(), binary=True)

    # sử dụng tập văn phạm | luật (*rule) để đoán nhận câu
    def get_form(self, *rules):
        result = []
        for rule in rules:
            result.append(rule.match(self))
        return result

    # biểu diễn câu
    def visual(self):
        nltk.ne_chunk(self.tag(), binary=True).draw()

    # đánh dấu một số thành phần đặc biệt trong câu, lấy theo regex
    def get_pattern(self, regex=r"""__________: {<.*>+}
                            }<VB.?|IN|DT|TO>+{"""):
        return nltk.RegexpParser(regex).parse(self.tag())

    #     trả về 1 vector số đại diện cho câu có dạng sau :
    #       ___________________768 chiều__________________________
    #     [ tensor([ 1.0497e+00, -6.3529e-01, ....  , -2.0922e+00]),    |
    #       tensor([ 1.0497e+00, -6.3529e-01, ....  , -2.0922e+00]),    |
    #       .                                                           số từ trong câu (theo thứ tự)
    #       .                                                           |
    #       .                                                           |
    #     ]
    def __abs__(self):
        return self.word_vector

    # trả dữ liệu về dạng dict:
    # {
    #     "text": câu đã được token và nối lại
    #     "word_vec": vector từ
    #     "vector":vector câu
    # }
    def to_json(self):
        return {
            "text": self.__str__(),
            "word_vec": [d.tolist() for d in self.word_vector],
            "vector": self.sentence_vector.tolist()
        }


class Question(Sentence):
    pass


# đoạn văn : là tập hợp các câu
class Paragrapth:
    # Khởi tạo đoạn văn bản với dữ liệu text| json
    def __init__(self, text="", json=None):
        if json is None:
            self.sentences = [Sentence(text=sen) for sen in tokenize.sent_tokenize(text)]
        else:
            self.sentences = [Sentence(json=json[j]) for j in json]
        self.iter = 0

    def __next__(self):
        try:
            result = self.sentences[self.iter]
            self.iter += 1
            return result
        except:
            raise StopIteration

    # phép toán cộng đoạn văn với đoạn văn, đoạn văn với câu ̣làm thay đổi giá trị đoạn hiện tại
    def __add__(self, sent_para):
        if isinstance(sent_para, Sentence):
            self.sentences.append(sent_para)
        else:
            if isinstance(sent_para, Paragrapth):
                for sen in sent_para.sentences:
                    self.sentences.append(sen)
            else:
                raise TypeError(sent_para.__class__.__name__ + " can not be added with a Paragraph")
        return self

    # nội dung dạng text của đoạn
    def __str__(self):
        return ' '.join([str(sentence) for sentence in self.sentences])

    # tập hợp các vector câu trong đoạn
    def __abs__(self):
        return [sentence.sentence_vector.tolist() for sentence in self.sentences]

    # trả dữ liệu dưới dạng list:
    # [
    #     câu 1,
    #     câu 2,...
    # ]
    def to_json(self):
        return [sent.to_json() for sent in self.sentences]

    def __getitem__(self, key):
        return self.sentences[key]


class Entry:
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

    def __str__(self):
        return '"question": {} \n"multi_abs_summ": {}\n"answer_ext_summ": {}'.format(str(self.question),
                                                                                     str(self.multi_abs_summ),
                                                                                     str(self.multi_ext_summ))

    # trả dữ liệu dưới dạng dict:
    # {
    #     "question": đoạn question
    #     "multi_abs_summ": đoạn tóm tắt abstract đa văn bản
    #     "multi_ext_summ": đoạn tóm tắt extract đa văn bản
    #     "answers": [
    #         {
    #             "answer_abs_summ": đoạn tóm tắt abstract đơn văn bản
    #             "answer_ext_summ": đoạn tóm tắt extract đơn văn bản
    #             "article": nội dung văn bản
    #             "rating": đánh giá
    #             <do section được làm thủ công nên em không đưa vào dữ liệu>
    #         }
    #     ]
    # }
    def to_json(self):
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
