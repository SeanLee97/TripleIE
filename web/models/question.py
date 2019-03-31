import json

from web.models.base import Base
from utils.common import format


class Question(Base):
    def __init__(self):
        super(Base, self).__init__()

    def save_question(self, question, norm_questions, triples):
        norm_questions = list(map(format, norm_questions))
        norm_questions = json.dumps({'norm_questions': norm_questions}, ensure_ascii=False)

        triples = list(map(format, triples))
        triples = json.dumps({'triples': triples}, ensure_ascii=False)

        insert_sql = ("INSERT INTO kb_questions (question,normalize_question,triples,create_time) "
                      "VALUES ('%s','%s','%s',NOW())" %
                      (question, norm_questions, triples))

        self.exec_sql(insert_sql)
