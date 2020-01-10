import random
from brain_games.const import BEGIN_RANDOM
from brain_games.const import END_RANDOM
from brain_games.const import ANSWER_STRING


def gcd():
    first_el = random.randint(BEGIN_RANDOM, END_RANDOM)
    second_el = random.randint(BEGIN_RANDOM, END_RANDOM)

    correct_ans = 1
    min_el = first_el if first_el < second_el else second_el
    for ii in range(1, min_el + 1):
        if first_el % ii == 0 and second_el % ii == 0:
            correct_ans = ii

    ANSWER_STRING['games']['question'] = '{} {}'.format(first_el, second_el)
    ANSWER_STRING['games']['answer_correct'] = str(correct_ans)
