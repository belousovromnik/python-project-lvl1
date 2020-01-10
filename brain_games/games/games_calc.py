import random
from brain_games.const import BEGIN_RANDOM
from brain_games.const import END_RANDOM
from brain_games.const import ANSWER_STRING


def calc():
    first_el = random.randint(BEGIN_RANDOM, END_RANDOM)
    second_el = random.randint(BEGIN_RANDOM, END_RANDOM)
    what_do = random.choice(['+', '-', '*'])

    correct_ans = 0
    if what_do == '+':
        correct_ans = first_el + second_el
    elif what_do == '-':
        correct_ans = first_el - second_el
    elif what_do == '*':
        correct_ans = first_el * second_el

    ANSWER_STRING['games']['question'] = '{} {} {}'.format(
        first_el,
        what_do,
        second_el)
    ANSWER_STRING['games']['answer_correct'] = str(correct_ans)
