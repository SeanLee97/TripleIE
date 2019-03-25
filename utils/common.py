def getQuestions(dir):
    questions = []
    with open(dir, 'r', encoding='utf-8') as f:
        for line in f:
            questions.append(line.strip())

    return questions
