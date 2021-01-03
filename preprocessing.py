from base_type import Entry
import json
from sklearn.cluster import AgglomerativeClustering
from base_type import Paragrapth
import os

LINK_TO_INPUT = 'DATA/question_driven_answer_summarization_primary_dataset.json'
LINK_TO_OUTPUT = 'DATA/question_driven_answer_summarization_primary_dataset_output.json'
LINK_TO_TEMPLATE_FILE = 'DATA/template.txt'

# phâp cụm phâm cấp: 1 đoạn văn -> n đoạn văn
def para_clustering(para, clusters=3, distance='euclidean'):
    clustering = AgglomerativeClustering(n_clusters=clusters, affinity=distance).fit(abs(para))
    result = [Paragrapth() for i in range(clusters)]
    count = -1
    for label in clustering.labels_:
        count += 1
        result[label] += para[count]
    return result


class Preprocessing:

    data = json.load(open(LINK_TO_INPUT))
    output = []

    def save(self):
        pr = False
        self.output = []
        if os.path.exists(LINK_TO_OUTPUT) and os.path.getsize(LINK_TO_OUTPUT) > 0:
            pass
        else:
            for ques_id in self.data:
                m = Entry(self.data[ques_id]).to_json()
                self.output.append(m)
                # if pr is False:
                #     print("done")
                #     with open(LINK_TO_OUTPUT, mode='w+') as f:
                #         json.dump(m, f)
                #         f.close()
                # return None
                #     for testing process , open these lines
            with open(LINK_TO_OUTPUT, mode='w+') as f:
                json.dump(self.output, f)
                f.close()
            print("successfully saving data!")

    def __init__(self):
        self.save()
        self.output = json.load(open(LINK_TO_OUTPUT, mode='r'))


