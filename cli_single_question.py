from utils.normalize import Normalize
from ie_single_question import TripleIE


class CliSingle():
    def __init__(self, sentence):
        self.sentence = sentence
        self.triples = []

    def run(self):
        sentences = Normalize(self.sentence).normalize()
        for sentence in sentences:
            triples = TripleIE(sentence, 'E:/Projects/PyCharmProjects/GitHub/TripleIE/ltp_data').run()
            for triple in triples:
                self.triples.append(triple)

        return self.triples


if __name__ == "__main__":
    cli = CliSingle('1984年上海的平均农村人口和平均城镇人口')
    print(cli.run())
