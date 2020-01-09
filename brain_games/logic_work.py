import random
from brain_games.cli import run


def is_even():
    COUNT_QUESTIONS = 3
    CORRECT_ANSWER_YES = 'yes'
    CORRECT_ANSWER_NO = 'no'
    BEGIN_RANDOM = 1
    END_RANDOM = 100

    nam_user = run('May I have your name? ')
    print("Hello, {}!". format(nam_user))

    i = 1
    while i <= COUNT_QUESTIONS:
        cnt = random.randint(BEGIN_RANDOM, END_RANDOM)
        print('Question: {}'.format(cnt))
        answer = run('Your answer: ')
        answer = answer.lower()

        correct_ans = ''
        if cnt % 2 == 0:
            correct_ans = 'yes'
        elif cnt % 2 == 1:
            correct_ans = 'no'

        if correct_ans == CORRECT_ANSWER_YES and answer == CORRECT_ANSWER_YES:
            print('Correct!')
        elif correct_ans == CORRECT_ANSWER_NO and answer == CORRECT_ANSWER_NO:
            print('Correct!')
        else:
            txt = "'{}' is wrong answer ;(.".format(answer)
            txt += "Correct answer was '{}'.".format(correct_ans)
            print(txt)
            print("Let's try again, {}!".format(nam_user))
            break
        i += 1
    else:
        print("Congratulations, {}!".format(nam_user))
