from brain_games.cli import welcome, correct, incorrect, congratulations
from brain_games.cli import question
from brain_games.const import COUNT_QUESTIONS
from brain_games.const import ANSWER_STRING

from brain_games.games.games_prime import prime
from brain_games.games.games_progression import progression
from brain_games.games.games_gcd import gcd
from brain_games.games.games_even import is_even
from brain_games.games.games_calc import calc


def games(nam_games):
    nam_user = welcome(ANSWER_STRING[nam_games]['welcome'])

    i = 1
    while i <= COUNT_QUESTIONS:
        if nam_games == 'prime':
            prime()
        elif nam_games == 'progression':
            progression()
        elif nam_games == 'gcd':
            gcd()
        elif nam_games == 'even':
            is_even()
        elif nam_games == 'calc':
            calc()

        answer = question(ANSWER_STRING['games']['question'])
        if ANSWER_STRING['games']['answer_correct'] == answer:
            correct()
        else:
            incorrect(
                answer,
                ANSWER_STRING['games']['answer_correct'],
                nam_user)
            break
        i += 1
    else:
        congratulations(nam_user)
