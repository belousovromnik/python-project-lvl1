import prompt


def run(str='Welcome to the Brain Games!'):
    return prompt.string(str)


def welcome(what_todo):
    print('Welcome to the Brain Games!!!')
    print(what_todo)

    nam_user = prompt.string('May I have your name? ')
    print("Hello, {}!". format(nam_user))
    return nam_user


def correct(strr='Correct!'):
    print(strr)


def incorrect(answer, correct_ans, nam_user):
    txt = "'{}' is wrong answer ;(.".format(answer)
    txt += "Correct answer was '{}'.".format(correct_ans)
    print(txt)
    print("Let's try again, {}!".format(nam_user))


def congratulations(nam_user):
    print("Congratulations, {}!".format(nam_user))
