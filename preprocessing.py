from base_type import Entry
import json


class Preprocessing:
    LINK_TO_INPUT = 'DATA/question_driven_answer_summarization_primary_dataset.json'
    LINK_TO_OUTPUT = 'DATA/question_driven_answer_summarization_primary_dataset_output.json'
    data = json.load(open(LINK_TO_INPUT))
    output = []

    def save(self):
        self.output = []
        for ques_id in self.data:
            m = Entry(self.data[ques_id]).to_json()
            self.output.append(m)
            print(m)
        with open(self.LINK_TO_OUTPUT, mode='w+') as f:
            json.dumps(self.output, f)
            f.close()

    def __init__(self):
        self.save()
        self.output = json.load(open(self.LINK_TO_OUTPUT, mode='r'))


x = Preprocessing()
