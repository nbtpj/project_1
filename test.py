# add your code to test here
import json
from preprocessing import LINK_TO_INPUT
from base_type import *
#
# data = json.load(open(LINK_TO_INPUT))
#
# for ques_id in data:
#     print(Sentence(data[ques_id]['question']).n_of_nouns)
con = True
while con:
    sen = Sentence(input("Enter your sentence: "))
    if sen is None:
        con = False
    else:
        print(sen.pos_tag())
        print('n_of_nouns: ', sen.n_of_nouns)
        print('n_of_numerals: ', sen.n_of_numerals)
