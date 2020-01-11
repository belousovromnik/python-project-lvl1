import random
from brain_games.const import BEGIN_RANDOM
from brain_games.const import END_RANDOM


def greeting():
    return 'What number is missing in the progression?'


def main_action():
    LONG_PROGRESSION = 10
    POSITION_QUE = random.randint(1, LONG_PROGRESSION)
    PROGRESSION_ITER = random.randint(1, LONG_PROGRESSION)
    first_el = random.randint(BEGIN_RANDOM, END_RANDOM)

    prog = [str(first_el), ]
    correct_ans = 0
    for ii in range(1, LONG_PROGRESSION + 1):
        if ii == POSITION_QUE:
            prog.append('..')
            correct_ans = first_el + PROGRESSION_ITER * ii
        else:
            prog.append(str(first_el + PROGRESSION_ITER * ii))

    str_to_question = ' '.join(prog)
    correct_ans = str(correct_ans)

    return str_to_question, correct_ans
