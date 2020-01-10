import random
from brain_games.const import BEGIN_RANDOM
from brain_games.const import END_RANDOM
from brain_games.const import ANSWER_STRING


def is_even():
    cnt = random.randint(BEGIN_RANDOM, END_RANDOM)

    correct_ans = ''
    if cnt % 2 == 0:
        correct_ans = 'yes'
    elif cnt % 2 == 1:
        correct_ans = 'no'

    ANSWER_STRING['games']['question'] = str(cnt)
    ANSWER_STRING['games']['answer_correct'] = correct_ans
