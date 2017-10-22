def Questions():
    mdnbuiltinobjects = {

        '':
        ""

        }

    questions = {}
    for dictionary in list(dir()):
        questions.update(eval(dictionary+".items()"))
    return questions
