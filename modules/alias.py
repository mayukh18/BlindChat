import random


NOUNS_FEMALE="../data/nouns_female"
NOUNS_MALE="../data/nouns_male"
PREFIXES="../data/prefixes"
SUFFIXES="../data/suffixes"


def generate_alias(gender):
    noun = ""
    prefix = ""
    suffix = ""
    if gender == "male":
        noun = _get_random_element(NOUNS_MALE)
    else:
        noun = _get_random_element(NOUNS_FEMALE)
    if _toss_a_coin():
        prefix = _get_random_element(PREFIXES)
    else:
        suffix = _get_random_element(SUFFIXES)
    return '{0}{1}{2}'.format(prefix, noun, suffix)


def _get_random_element(filename):
    with open(filename) as f:
        return random.choice(f.readlines()).strip()


def _toss_a_coin():
    return random.randint(0, 1) == 0
