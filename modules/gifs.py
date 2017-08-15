_male_start_hi = ['https://media.giphy.com/media/dzaUX7CAG0Ihi/giphy-downsized.gif',
                  'https://media.giphy.com/media/oJiCqvIqPZE3u/giphy.gif']

_female_start_hi = ['https://media.giphy.com/media/a1QLZUUtCcgyA/giphy-downsized.gif',
                    'https://media.giphy.com/media/EPJZhOrStSpz2/giphy-downsized.gif']

import random
def get_start_hi(gender):
    if gender == "male":
        #return random.choice(_male_start_hi)
        return _male_start_hi[1]
    elif gender == "female":
        #return random.choice(_female_start_hi)
        return _female_start_hi[1]
    else:
        return random.choice(_male_start_hi)