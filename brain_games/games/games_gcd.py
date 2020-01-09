import random
import prompt
from brain_games.cli import welcome, correct, incorrect, congratulations
from brain_games.const import COUNT_QUESTIONS
from brain_games.const import BEGIN_RANDOM
from brain_games.const import END_RANDOM


def gcd():
    nam_user = welcome('Find the greatest common divisor of given numbers.')

    i = 1
    while i <= COUNT_QUESTIONS:
        first_el = random.randint(BEGIN_RANDOM, END_RANDOM)
        second_el = random.randint(BEGIN_RANDOM, END_RANDOM)

        strr = '{} {}'.format(first_el, second_el)
        print('Question: {}'.format(strr))
        answer = prompt.integer('Your answer: ')

        correct_ans = 1
        min_el = first_el if first_el < second_el else second_el
        for ii in range(1, min_el + 1):
            if first_el % ii == 0 and second_el % ii == 0:
                correct_ans = ii

        if correct_ans == answer:
            correct()
        else:
            incorrect(answer, correct_ans, nam_user)
            break
        i += 1
    else:
        congratulations(nam_user)
