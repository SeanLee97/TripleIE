import sys

from flask import Flask, request, jsonify, render_template

sys.path.append('/home/httpd/TripleIE')

from cli_single_question import CliSingle
from web.models.question import Question

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/get_triples', methods=["POST"])
def get_triples():
    post = request.json
    question = post['q']
    triples, norm_questions = CliSingle(question).run()

    # 记录问题
    Question().save_question(question, norm_questions, triples)

    return jsonify(code=200, message='ok', data={'triples': triples})


@app.route('/get_test', methods=["POST"])
def get_test():
    return jsonify(code=200, message='ok', data={'triples': 111})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
