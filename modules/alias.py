import random

_SIZE_DESCRIPTORS = [
    'huge', 'small', 'enormous', 'big',
    'giant', 'tiny', 'massive', 'little'
]
_ADJECTIVE_DESCRIPTORS = [
    'lonely', 'calm', 'awesome', 'enhanced', 'depressed', 'drunk',
    'sober', 'great', 'noble', 'studious', 'cold', 'playful',
    'fun', 'crazy', 'shrewd', 'basic', 'gutsy', 'cute',
    'innocent', 'naughty', 'mischievous', 'smart',
    'tricky', 'unique', 'naive', 'drowzy', 'hot', 'sassy',
    'massive', 'puzzled', 'rare', 'spooky', 'lethal',
    'macho', 'lazy', 'kind', 'honourable', 'hungry', 'happy',
    'average', 'sleepy', 'grumpy', 'silent', 'shy',
    'needy', 'classy', 'scary', 'vain', 'early', 'soft'
    'deep', 'sweet', 'wild', 'light', 'dark', 'super',
    'brave', 'broad', 'broken', 'colossal', 'square',
    'muddy', 'mute', 'noisy', 'odd', 'old', 'young',
    'gentle', 'cool', 'broken', 'bold', 'bitter',
    'bubbly', 'broad', 'curly', 'ancient', 'aged',
    'damp', 'petite', 'snowy', 'soft', 'shiny',
    'slimy', 'sticky', 'gross', 'early', 'spring',
    'solitary', 'needy', 'deep', 'royal', 'round', 'rough',
    'restless', 'rapid', 'quiet', 'proud', 'polished',
    'lucky', 'jolly', 'lively', 'icy', 'legendary',
    'frosty', 'fragrant', 'flat', 'jiggly', 'fancy',
    'delicate', 'misty'
]

_COLOR = [
    'gray', 'yellow', 'orange', 'white', 'black',
    'blue', 'green', 'crimson', 'red', 'purple',
    'cyan', 'azure', 'cerulean', 'teal', 'pink',
    'aqua'
]
_ACTION_DESCRIPTORS = [
    'terrifying', 'roaring', 'soaring',
    'sparkling', 'daring', 'falling',
    'jumping'
]

_NAMES_MALE = [
    'Leo', 'Thor', 'Caspian', 'Ash',
    'Luke', 'Don', 'Mufasa', 'Duke',
    'Goku', 'Lucifer', 'Simba', 'Anakin',
    'Jack', 'Joe', 'Solomon', 'Nero',
    'Nemo', 'King', 'Emperor', 'Robin',
    'Ram', 'Prince', 'Ronin', 'Count',
    'Lord', 'Jarvis'
]

_NAMES_FEMALE = [
    'Lili', 'Lilith', 'Rihanna', 'Alexa', 'Cortana'
    'Mermaid', 'Madona', 'Lioness',
    'Eve', 'Rose', 'Princess', 'Queen',
    'huntress', 'vixen', 'Ivy', 'Minx',
    'Nova', 'Daisy', 'Lady', 'raven',
    'gal', 'goddess', 'emma', 'dora',
    'ariana', 'mistress', 'highness',
    'babe', 'tomboy', 'bride', 'doll',
    'empress'
]

_NAMES_UNISEX = [
    'Eagle', 'Bull', 'Fox', 'Vixen',
    'Stallion', 'Cheetah', 'Lion',
    'Tiger', 'Monkey', 'Frog', 'Horse',
    'Hippo', 'Hawk', 'Wizard', 'Witch',
    'Bull', 'Buck', 'Captain', 'Arrow',
    'Trump', 'Cyborg', 'Wolverine',
    'Spider', 'Bat', 'Bandit', 'Panther',
    'Cat', 'Joker', 'Necromancer', 'Devil',
    'Demon', 'Warlock', 'Mage', 'Warden',
    'Ant', 'Vader', 'Stark', 'Lannister',
    'Baratheon', 'Greyjoy', 'Sailor',
    'General', 'Captain', 'Corporal',
    'Cyclops', 'Tully',
    'Phasma', 'Bird', 'Birb', 'ninja',
    'Sargeant', 'Detective', 'snake',
    'serpent', 'sherlock', 'watson',
    'house', 'gambit', 'sailor',
    'baratheon', 'doom', 'doomsday',
    'warden', 'warrior', 'waffles',
    'candy', 'Swift', 'Butterfly',
    'Monroe', 'moon', 'dove', 'dawn',
    'sunflower', 'mist', 'snail',
    'zebra', 'unicorn', 'seahorse',
    'squirrel', 'storm', 'banshee',
    'flower', 'angel', 'beauty', 'artist'
]

_suffixes = [
    'OfAdua', 'OfAtlantis', 'OfCimmeria', 'OfDarkWood', 'OfDune',
    'OfEgypt', 'OfLalaland', 'OfMidgard', 'OfNowhere', 'OfOz',
    'OfSparta', 'OfTheDesert', 'OfTheForest', 'OfTheFuture',
    'OfTheIsland', 'OfTheJungle', 'OfTheLand', 'OfTheSea',
    'OfTheWorld', 'TheAgeless', 'TheBabyface', 'TheBarbarian',
    'TheBetrayer', 'TheBrave', 'TheDestroyer', 'TheGhost',
    'TheGreat', 'TheHammer', 'TheLionheart', 'TheOld', 'TheQuiet',
    'TheSecond', 'TheShadow', 'TheTall', 'TheTemplar',
    'TheTraveler', 'TheWanderer', 'TheWeakest', 'TheWise',
    'UnderThePass', 'ofTheBay', 'ofTheDay', 'ofTheNight'
]

_NAMES = {
    'male': _NAMES_MALE,
    'female': _NAMES_FEMALE
}
DESCRIPTORS = _ADJECTIVE_DESCRIPTORS + _SIZE_DESCRIPTORS


def random_noun(gender):
    return random.choice(_NAMES_UNISEX + _NAMES[gender])


def random_descriptor(noun):
    return random.choice(DESCRIPTORS) if (noun not in _NAMES_UNISEX) else random.choice(DESCRIPTORS + _ACTION_DESCRIPTORS)


def random_color():
    return random.choice(_COLOR)


def random_suffix():
    return random.choice(_suffixes)


format = lambda *array: "".join(map(lambda word: word[0].upper() + word[1:], array))


def generate_alias(gender, size=30):
    noun = random_noun(gender)
    descriptor = random_descriptor(noun)
    color = random_color()
    suffix = random_suffix()
    if len(color + descriptor + noun + suffix) <= size:
        return format(color, descriptor, noun, suffix)
    elif len(descriptor + noun + suffix) <= size:
        return format(descriptor, noun, suffix)
    elif len(noun + suffix) <= size:
        return format(noun, suffix)
    elif len(descriptor + noun) <= size:
        return format(descriptor, noun)
    else:
        return format(noun)[:size]


for i in range(100):
    print(generate_alias(random.choice(['male', 'female']), random.randrange(10, 30)))
