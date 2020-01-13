import random
from operator import add, sub, mul
from brain_games.constants import MINIMAL_RANDOM
from brain_games.constants import MAXIMAL_RANDOM


def greeting():
    return 'What is the result of the expression?'


def main_action():
    first_el = random.randint(MINIMAL_RANDOM, MAXIMAL_RANDOM)
    second_el = random.randint(MINIMAL_RANDOM, MAXIMAL_RANDOM)
    operator_dict = {'+': add, '-': sub, '*': mul}

    what_do = random.choice(list(operator_dict))
    correct_ans = operator_dict[what_do](first_el, second_el)

    str_to_question = '{} {} {}'.format(
        first_el,
        what_do,
        second_el)
    correct_ans = str(correct_ans)

    return str_to_question, correct_ans
