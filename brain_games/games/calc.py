import random
from brain_games.const import BEGIN_RANDOM
from brain_games.const import END_RANDOM


def greeting():
    return 'What is the result of the expression?'


def main_action():
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

    str_to_question = '{} {} {}'.format(
        first_el,
        what_do,
        second_el)
    correct_ans = str(correct_ans)

    return str_to_question, correct_ans
