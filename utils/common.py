def getQuestions(dir):
    questions = []
    with open(dir, 'r', encoding='utf-8') as f:
        for line in f:
            questions.append(line.strip())

    return questions


def getTriples(dir):
    triples = []
    with open(dir, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            line_sp = line.strip()
            line_list = line_sp.split('\t')
            triples.append({
                'id': line_list[0],
                'triples': line_list[2]})

    return triples


def getTriplesWithId(id, triples):
    list = []
    for triple in triples:
        if triple['id'] == str(id):
            list.append(triple['triples'])

    return list
