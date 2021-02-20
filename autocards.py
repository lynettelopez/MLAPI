from pipelines import qg_pipeline
from transformers import pipeline
from bs4 import BeautifulSoup
import csv


class Autocards:
    def __init__(self):
        self.qg = qg_pipeline('question-generation', model='valhalla/t5-base-qg-hl', ans_model='valhalla/t5-small-qa-qg-hl')
        self.qa_pairs = []

    def consume_text(self, text, per_paragraph=False):
        text = text.replace('\xad ', '')

        if per_paragraph:
            for paragraph in text.split('\n\n'):
                self.qa_pairs += self.qg(paragraph)
        else:
            text = text.replace('\n\n', '. ').replace('..', '.')
            self.qa_pairs += self.qg(text)

    def consume_text_file(self, filename):
        self.consume_text(open(filename).read())

    def consume_paper(self, filename):
        soup = BeautifulSoup(open(filename), 'xml')
        paragraphs = []

        for paragraph in soup.article.body.find_all('p'):
            paragraph = ' '.join(paragraph.get_text().split())
            if len(paragraph) > 40:
                paragraphs += [paragraph]

        qa_pairs = []
        for paragraph in paragraphs:
            qa_pairs += self.qg(paragraph)

        self.qa_pairs += qa_pairs

    def clear(self):
        self.qa_pairs = []

    def print(self, prefix='', jeopardy=False):
        if prefix != '':
            prefix += ' '
            
        for qa_pair in self.qa_pairs:
            if jeopardy:
                print('\"' + prefix + qa_pair['answer'] + '\",\"' + qa_pair['question'] + '\"')
            else:
                print('\"' + prefix + qa_pair['question'] + '\",\"' + qa_pair['answer'] + '\"')

    def export(self, filename, prefix='', jeopardy=False):
        if prefix != '':
            prefix += ' '

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for qa_pair in self.qa_pairs:
                if jeopardy:
                    writer.writerow([prefix + qa_pair['answer'], qa_pair['question']])
                else:
                    writer.writerow([prefix + qa_pair['question'], qa_pair['answer']])
