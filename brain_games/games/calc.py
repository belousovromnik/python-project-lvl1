import random
from operator import add, sub, mul
from brain_games.constants import MINIMAL_RANDOM, MAXIMAL_RANDOM


def greeting():
    return 'What is the result of the expression?'


def main_action():
    first_el = random.randint(MINIMAL_RANDOM, MAXIMAL_RANDOM)
    second_el = random.randint(MINIMAL_RANDOM, MAXIMAL_RANDOM)
    symbol, function = random.choice((
        ('+', add),
        ('-', sub),
        ('*', mul)
    ))
    correct_ans = function(first_el, second_el)

    str_to_question = '{} {} {}'.format(
        first_el,
        symbol,
        second_el)
    correct_ans = str(correct_ans)

    return str_to_question, correct_ans
