from json import load

with open('quiz.json', encoding='utf8') as questions_file:
    questions = load(questions_file)
    print(questions)