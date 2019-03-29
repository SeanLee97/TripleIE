with open('normalize.txt', 'r', encoding='utf-8') as q:
    questions = q.readlines()

triples = []
with open('normalize_out.txt', 'r', encoding='utf-8') as triple:
    for line in triple:
        line_sp = line.strip()
        line_list = line_sp.split('\t')
        triples.append({
            'q_id': line_list[0],
            'triple': line_list[2]
        })

with open('format_output.txt', 'a+', encoding='utf-8') as format:
    for index, question in enumerate(questions):
        q_line = question.strip()
        format.write(str(index + 1) + ' ' + q_line + '\n')
        for triple in triples:
            if triple['q_id'] == str(index + 1):
                format.write('\t' + triple['triple'] + '\n')
