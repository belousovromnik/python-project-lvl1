import random
import prompt
from brain_games.cli import welcome, correct, incorrect, congratulations
from brain_games.const import COUNT_QUESTIONS
from brain_games.const import BEGIN_RANDOM
from brain_games.const import END_RANDOM


def progression():
    nam_user = welcome('Find the greatest common divisor of given numbers.')

    i = 1
    while i <= COUNT_QUESTIONS:
        LONG_PROGRESSION = 10
        POSITION_QUE = random.randint(1, LONG_PROGRESSION + 1)
        PROGRESSION_ITER = random.randint(1, LONG_PROGRESSION + 1)
        first_el = random.randint(BEGIN_RANDOM, END_RANDOM)

        prog = [str(first_el), ]
        correct_ans = 0
        for ii in range(1, LONG_PROGRESSION):
            if ii == POSITION_QUE:
                prog.append('..')
                correct_ans = first_el + PROGRESSION_ITER * ii
            else:
                prog.append(str(first_el + PROGRESSION_ITER * ii))

        strr = ' '.join(prog)
        print('Question: {}'.format(strr))
        answer = prompt.integer('Your answer: ')

        if correct_ans == answer:
            correct()
        else:
            incorrect(answer, correct_ans, nam_user)
            break
        i += 1
    else:
        congratulations(nam_user)
