import random
import prompt
from brain_games.cli import welcome, correct, incorrect, congratulations
# from brain_games.cli import run, welcome
from brain_games.const import COUNT_QUESTIONS
# from brain_games.const import CORRECT_ANSWER_NO
# from brain_games.const import CORRECT_ANSWER_YES
from brain_games.const import BEGIN_RANDOM
from brain_games.const import END_RANDOM


def calc():
    nam_user = welcome('What is the result of the expression?')

    i = 1
    while i <= COUNT_QUESTIONS:
        first_el = random.randint(BEGIN_RANDOM, END_RANDOM)
        second_el = random.randint(BEGIN_RANDOM, END_RANDOM)
        what_do = random.choice(['+', '-', '*'])

        strr = '{} {} {}'.format(first_el, what_do, second_el)
        print('Question: {}'.format(strr))
        answer = prompt.integer('Your answer: ')

        correct_ans = 0
        if what_do == '+':
            correct_ans = first_el + second_el
        elif what_do == '-':
            correct_ans = first_el - second_el
        elif what_do == '*':
            correct_ans = first_el * second_el

        if correct_ans == answer:
            correct()
        else:
            incorrect(answer, correct_ans, nam_user)
            break
        i += 1
    else:
        congratulations(nam_user)
