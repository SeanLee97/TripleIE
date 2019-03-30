import sys
import time

from flask import Flask, request, jsonify, render_template

sys.path.append('/home/httpd/TripleIE')

from cli_single_question import CliSingle

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/get_sparql', methods=["POST"])
def get_triples():
    question = request.form.get('q')
    rs = CliSingle(question).run()

    # 记录问题
    file_name = 'log/questions_' + time.strftime('%Y_%m_%d', time.localtime(time.time())) + '.txt'
    with open(file_name, 'a+', encoding='utf-8') as f:
        f.write(question + '\n')

    return jsonify(code=200, message='ok', data={'triples': rs})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
