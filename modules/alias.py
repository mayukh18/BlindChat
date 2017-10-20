_adjectives = [
        'Aged', 'Ancient', 'Bubbly', 'Bitter', 'Black', 'Blue', 'Bold', 'Brave',
        'Broad', 'Broken', 'Calm', 'Cold','Colossal', 'Cool', 'Crimson', 'Curly', 'Damp',
        'Dark', 'Daring', 'Delicate', 'Falling', 'Fancy', 'Super', 'Jiggly',
        'Flat', 'Fragrant', 'Frosty', 'Gentle', 'Green', 'Legendary',
        'Icy', 'Jolly', 'Jumping', 'Little', 'Lively', 'Lucky', 'Lonely',
        'Muddy', 'Mute', 'Noisy', 'Odd', 'Old', 'Orange', 'Polished', 'Proud',
        'Purple', 'Quiet', 'Rapid', 'Red', 'Restless', 'Rough', 'Round', 'Royal', 'Shiny',
        'Shy', 'Silent', 'Small', 'Snowy', 'Soft', 'Solitary', 'Sparkling', 'Spring',
        'Square', 'Super', 'Sweet', 'Tight', 'Tiny', 'White', 'Wild', 'Yellow', 'Young', 'Sticky',
        'Fluffy', 'Petite', 'Grumpy', 'Happy', 'Sleepy', 'Gray', 'Average', 'Hungry', 'Honorable',
        'Kind', 'Lazy', 'Lethal', 'Macho', 'Massive', 'Puzzled', 'Rare', 'Spooky', 'Sassy', 'Tricky',
        'Unique', 'Naive', 'Drowzy', 'Hot', 'Innocent', 'Naughty', 'Mischievous', 'Smart', 'Fun',
        'Crazy', 'Shrewd', 'Basic', 'Gutsy', 'Cute', 'Drunk', 'Sober', 'Depressed', 'Slimy', 'Gross',
        'Needy', 'Dark', 'Light', 'Roaring', 'Soaring', 'Noble', 'Vain', 'Terrifying', 'Scary',
        'Studious', 'Huge', 'Enormous', 'Big', 'Giant', 'Great', 'Playful', 'Classy', 'Cold'
    ]

_nouns_male = [
        'King', 'Prince', 'Bandit', 'Hulk', 'Thor', 'Leo', 'Deadpool', 'Trump',
        'Moustache', 'Arrow', 'Caspian', 'Horse', 'Frog', 'Monkey', 'Lion',
        'Tiger', 'Cheetah', 'Eagle', 'Wizard', 'Hawk', 'Jack', 'Hippo' , 'Stallion' , 'Bull' , 'Buck',
        'Emperor','Ram', 'Captain', 'Batman', 'Robin', 'Deathstroke', 'Cyborg', 'Wolverine', 'Spiderman', 
        'Flash', 'Panther', 'Daredevil', 'Ironman', 'Joker', 'Aquaman', 'Necromancer', 'Warlock', 'Magneto',
        'Gambit', 'Cyclops', 'Ronin', 'Warden', 'Duke', 'Lord', 'Darth', 'Vader', 'Goku', 'Gohan', 'Broly',
        'Ash', 'Antman', 'Doom', 'General', 'Snake', 'Devil', 'Sergeant', 'Detective', 'Demon', 'Birdman',
        'Jarvis', 'Ultron', 'Stark', 'Lannister', 'Baratheon', 'Tully', 'Greyjoy', 'Tarth', 'Phasma',
        'Sailor', 'Mufasa', 'Simba', 'Ninja', 'Swordsman', 'Don', 'Gangster', 'Superman', 'Doomsday',
        'Lucifer', 'Serpent', 'Count'
    ]

_nouns_female = [
        'Alexa','Lili', 'Princess', 'Rihanna', 'Swift', 'Queen', 'LaserGirl', 'Mermaid',
        'Butterfly', 'Batgirl', 'Madonna', 'Foxie', 'Lioness', 'Monroe', 'Eve', 'Xiry',
        'Snail', 'Unicorn', 'Moon', 'Dove', 'Witch', 'Rose', 'Zebra', 'Seahorse', 'Squirrel' , 'Doe', 'Empress',
        'Vixen', 'Widow', 'Supergirl', 'Storm', 'Catwoman', 'WonderWoman', 'Hawkgirl', 'Amazon', 'Mystique', 'Raven',
        'Banshee', 'Enchantress', 'Ivy', 'Minx', 'Nova', 'Duchess', 'Bachelorette', 'Cat', 'Flower', 'Daisy',
        'Sunflower', 'Lady', 'Mist', 'Misty', 'Superwoman', 'Gal', 'Dynamo', 'Connoisseur', 'Huntress', 
        'Angel', 'Goddess', 'Mystery', 'Maiden', 'Dame', 'Damsel', 'Beauty', 'Artist', 'Chick', 'Snake',
        'Heroine', 'Tomboy', 'Doll', 'Spinster', 'Bride', 'Countess', 'Babe', 'Dora', 'Mistress', 'Highness'
    ]

import random

def generate_alias(gender):
    adj = random.choice(_adjectives)
    if gender == "male":
        noun = random.choice(_nouns_male)
    else:
        noun = random.choice(_nouns_female)

    return adj+noun