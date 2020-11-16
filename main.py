# This is a sample Python script.

# from googletrans import Translator
# ques = []
# tr = Translator()
from googletrans import Translator
import json
import pickle

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# to create a file.
tr = Translator()
ques = []
ans = []
# get data converted to lists:

with open('ques_ans_o.json', 'r') as jsonofabitch:
    qa = json.load(jsonofabitch)  # xD (inspired from aryaman)
for q, a in qa.items():
    ques.append(q)
    ans.append(a)

def convert_text(answers, questions):
    translations_ans = tr.translate(list(answers), dest='hi')
    translations_ques = tr.translate(list(questions), dest='hi')
    ans_hindi = []
    ques_hindi = []
    for ta in translations_ans:
        ans_hindi.append(ta.text)
    for tq in translations_ques:
        ques_hindi.append(tq.text)
    return ans_hindi, ques_hindi


# answers = ('how are you','mother where are you','My brother is talking on the phone')
# Press the green button in the gutter to run the script.
def write_text(quest, answ):
    ans_hindi, ques_hindi = convert_text(answ, quest)

    with open('questions.txt', 'wb') as fh:
        pickle.dump(ques_hindi, fh)
    with open('answers.txt', 'wb') as fh:
        pickle.dump(ans_hindi, fh)


if __name__ == '__main__':
    # print_hi('PyCharm')
    write_text(ques, ans)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
