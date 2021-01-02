from base_type import Entry
import json


class Preprocessing:
    LINK_TO_INPUT = 'DATA/question_driven_answer_summarization_primary_dataset.json'
    LINK_TO_OUTPUT = 'DATA/question_driven_answer_summarization_primary_dataset_output.json'
    LINK_TO_TEMPLATE_FILE = 'DATA/template.txt'
    data = json.load(open(LINK_TO_INPUT))
    output = []

    def save(self):
        self.output = []
        for ques_id in self.data:
            m = Entry(self.data[ques_id]).to_json()
            self.output.append(m)
            with open(self.LINK_TO_TEMPLATE_FILE, mode='a+') as f:
                json.dump(m, f)
        #         for testing process , open these lines
        # with open(self.LINK_TO_OUTPUT, mode='w+') as f:
        #     json.dump(self.output, f)
        #     f.close()
        print("successfully saving data!")

    def __init__(self):
        self.save()
        self.output = json.load(open(self.LINK_TO_OUTPUT, mode='r'))


x = Preprocessing()
