import json
import os
from biobert_embedding import BiobertEmbedding
BERT = BiobertEmbedding()
LINK_TO_INPUT = 'DATA/question_driven_answer_summarization_primary_dataset.json'


def is_valid_sentence(text):
    m = text.split()
    if len(m) > 3:
        return True
    return False


class Sentence:
    def __init__(self, text=''):
        text = text.strip()
        self.data = dict()
        try:
            self.data['word_vector'] = [word_vec.tolist() for word_vec in BERT.word_vector(text)]
            self.data['sentence_vector'] = BERT.sentence_vector(text).tolist()
        except:
            m = text.split(',')
            self.data['word_vector'] = []
            for m_ in m:
                for x in m_.split('-'):
                    self.data['word_vector'].extend([word_vec.tolist() for word_vec in BERT.word_vector(x)])


    def save(self, file_name):
        json.dump(self.data, open(file_name, mode='w+'))


class Paragraph:
    def __init__(self, text=''):
        self.data = {}
        split_texts = [sentence_text for sentence_text in text.split('.') if is_valid_sentence(sentence_text)]
        for sentence_id in range(len(split_texts)):
            print('\t\t\t creating sentence :' + str(sentence_id))
            self.data[sentence_id] = Sentence(split_texts[sentence_id]).data


class Question:
    """A copy of raw data, has been processed (create new vectors)"""

    def __init__(self, js, ques_id):
        self.ques_id = ques_id
        if not os.path.exists('DATA/VECTOR/' + self.ques_id + '.json'):
            print('creating : question {}'.format(ques_id))
            self.data = dict()
            self.data['question'] = Paragraph(js["question"]).data
            self.data['multi_abs_summ'] = Paragraph(js["multi_abs_summ"]).data
            self.data['multi_ext_summ'] = Paragraph(js["multi_ext_summ"]).data
            self.data['answers'] = dict()
            for ans_id in js["answers"]:
                print('\t\t creating answer :' + str(ans_id))
                self.data['answers'][ans_id] = {
                    "answer_abs_summ": Paragraph(text=js["answers"][ans_id]["answer_abs_summ"]).data,
                    "answer_ext_summ": Paragraph(text=js["answers"][ans_id]["answer_ext_summ"]).data,
                    "article": Paragraph(text=js["answers"][ans_id]["article"]).data,
                    "rating": js["answers"][ans_id]["rating"]
                }
        else:
            self.data = json.load(open('DATA/VECTOR/' + self.ques_id + '.json', encoding='utf8'))
            print('loading : question {}'.format(ques_id))

    def get_sentence(self,ans_id, sen_id):
        return self.data['answers'][ans_id]['article'][sen_id]

    def save(self):
        if not os.path.exists('DATA/VECTOR/' + self.ques_id + '.json'):
            with open('DATA/VECTOR/' + self.ques_id + '.json', 'w+', encoding='utf8') as f:
                json.dump(self.data, f)


def get_data():
    with open(LINK_TO_INPUT, encoding='utf8', mode='r') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    data = get_data()
    for ques_id in data:
        Question(data[ques_id], ques_id).save()
