import random
from brain_games.constants import MINIMAL_RANDOM
from brain_games.constants import MAXIMAL_RANDOM


def greeting():
    return 'Find the greatest common divisor of given numbers.'


def main_action():
    first_el = random.randint(MINIMAL_RANDOM, MAXIMAL_RANDOM)
    second_el = random.randint(MINIMAL_RANDOM, MAXIMAL_RANDOM)

    correct_ans = 1
    min_el = first_el if first_el < second_el else second_el
    for ii in range(1, min_el + 1):
        if first_el % ii == 0 and second_el % ii == 0:
            correct_ans = ii

    str_to_question = '{} {}'.format(first_el, second_el)
    correct_ans = str(correct_ans)

    return str_to_question, correct_ans
