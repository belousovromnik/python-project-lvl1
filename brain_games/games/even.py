import random
from brain_games.const import BEGIN_RANDOM
from brain_games.const import END_RANDOM


def greeting():
    return 'Answer "yes" if number even otherwise answer "no".'


def main_action():
    cnt = random.randint(BEGIN_RANDOM, END_RANDOM)

    correct_ans = ''
    if cnt % 2 == 0:
        correct_ans = 'yes'
    elif cnt % 2 == 1:
        correct_ans = 'no'

    str_to_question = str(cnt)

    return str_to_question, correct_ans
