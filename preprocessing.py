import pickle
from base_type import Entry
import json


class Preprocessing:
    LINK_TO_INPUT = 'DATA/question_driven_answer_summarization_primary_dataset.json'
    LINK_TO_OUTPUT = 'DATA/question_driven_answer_summarization_primary_dataset_output.pickle'
    data = json.load(open(LINK_TO_INPUT))
    output = []

    def save(self):
        self.output = []
        for ques_id in self.data:
            m = Entry(self.data[ques_id])
            self.output.append(m)
            print(m)
        with open(self.LINK_TO_OUTPUT, mode='wb+') as f:
            pickle.dumps(self.output, f)
            f.close()

    def __init__(self):
        self.save()
        self.output = pickle.load(open(self.LINK_TO_OUTPUT, mode='rb'))


x = Preprocessing()
