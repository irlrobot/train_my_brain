#!/usr/bin/env python
"""
Train My Brain
github.com/irlrobot/train_my_brain

Categories:
1. word_jumble
2. spelling_backwords
3. simple_math
4. memory_game
5. simple_trivia
6. word_association
7. repeat
8. out_of_place
9. low_high_number
"""
def fuzzy_match_threshold(category):
    """determine the threshold for fuzzy matching"""
    if category == 'word_jumble':
        return 60
    if category == 'spelling_backwords':
        return 90
    if category == 'simple_math':
        return 100
    if category == 'memory_game':
        return 60
    if category == 'simple_trivia':
        return 60
    if category == 'word_association':
        return 60
    if category == 'repeat':
        return 60
    if category == 'out_of_place':
        return 60
    if category == 'low_high_number':
        return 100

QUESTIONS = [
    {
        "id": 1,
        "question": "What word can you spell with these letters:  P... C... M... A...",
        "answer": "Camp",
        "category": "word_jumble"
    },
    {
        "id": 2,
        "question": "What word can you spell with these letters:  J... P... U... M...",
        "answer": "Jump",
        "category": "word_jumble"
    },
    {
        "id": 3,
        "question": "What word can you spell with these letters:  I... K... N... P...",
        "answer": "Pink",
        "category": "word_jumble"
    },
    {
        "id": 4,
        "question": "What word can you spell with these letters:  K... R... W... O...",
        "answer": "Work",
        "category": "word_jumble"
    },
    {
        "id": 5,
        "question": "What word can you spell with these letters:  A... S... D... F",
        "answer": "Fads",
        "category": "word_jumble"
    },
    {
        "id": 6,
        "question": "What word can you spell with these letters:  M... R... T... I...",
        "answer": "Trim",
        "category": "word_jumble"
    },
    {
        "id": 7,
        "question": "What word can you spell with these letters:  U... L... P... P...",
        "answer": "Pulp",
        "category": "word_jumble"
    },
    {
        "id": 8,
        "question": "What word can you spell with these letters:  B... B... M... O...",
        "answer": "Bomb",
        "category": "word_jumble"
    },
    {
        "id": 9,
        "question": "What word can you spell with these letters:  I... P... E... P...",
        "answer": "Pipe",
        "category": "word_jumble"
    },
    {
        "id": 10,
        "question": "What word can you spell with these letters:  U... D... R... M...",
        "answer": "Drum",
        "category": "word_jumble"
    },
    {
        "id": 11,
        "question": "Spell the word... Cats... backwords.",
        "answer": "STAC",
        "category": "spelling_backwords"
    },
    {
        "id": 12,
        "question": "Spell the word... Puppy... backwords.",
        "answer": "YPPUP",
        "category": "spelling_backwords"
    },
    {
        "id": 13,
        "question": "Spell the word... Rabbit... backwords.",
        "answer": "TIBBAR",
        "category": "spelling_backwords"
    },
    {
        "id": 14,
        "question": "Spell the color... Blue... backwords.",
        "answer": "EULB",
        "category": "spelling_backwords"
    },
    {
        "id": 15,
        "question": "Spell the word... Range... backwords.",
        "answer": "EGNAR",
        "category": "spelling_backwords"
    },
    {
        "id": 16,
        "question": "Spell the word... Monday... backwords.",
        "answer": "YADNOM",
        "category": "spelling_backwords"
    },
    {
        "id": 17,
        "question": "Spell the word... Basket... backwords.",
        "answer": "TEKSAB",
        "category": "spelling_backwords"
    },
    {
        "id": 18,
        "question": "Spell the word... Shoe... backwords.",
        "answer": "EOHS",
        "category": "spelling_backwords"
    },
    {
        "id": 19,
        "question": "Spell the word... Fruit... backwords.",
        "answer": "TIURF",
        "category": "spelling_backwords"
    },
    {
        "id": 20,
        "question": "Spell the word... Pasta... backwords.",
        "answer": "ATSAP",
        "category": "spelling_backwords"
    },
    {
        "id": 21,
        "question": "What does 4... plus... 8... minus... 2... equal?",
        "answer": "10",
        "category": "simple_math"
    },
    {
        "id": 22,
        "question": "What does 3... minus... 2... minus... 3... plus... 2... equal?",
        "answer": "0",
        "category": "simple_math"
    },
    {
        "id": 23,
        "question": "What does 10... times... 2... plus... 5... minus... 1... equal?",
        "answer": "24",
        "category": "simple_math"
    },
    {
        "id": 24,
        "question": "What does 2... times... 8... minus... 10... minus... 1... equal?",
        "answer": "5",
        "category": "simple_math"
    },
    {
        "id": 25,
        "question": "What does 10... plus... 50... plus... 25... minus... 7... equal?",
        "answer": "78",
        "category": "simple_math"
    },
    {
        "id": 26,
        "question": "What does 100... minus... 42... mius 13... minus... 10... equal?",
        "answer": "35",
        "category": "simple_math"
    },
    {
        "id": 27,
        "question": "What does 10... times... 10... minus... 9... equal?",
        "answer": "91",
        "category": "simple_math"
    },
    {
        "id": 28,
        "question": "What does 4... plus... 9... plus... 5... times... 3... equal?",
        "answer": "54",
        "category": "simple_math"
    },
    {
        "id": 29,
        "question": "What does 37... minus... 8... plus... 19... equal?",
        "answer": "48",
        "category": "simple_math"
    },
    {
        "id": 30,
        "question": "What does 120... times... 2... plus... 50... minus... 11... equal?",
        "answer": "279",
        "category": "simple_math"
    },
    {
        "id": 31,
        "question": "Sara went to the movies on Thursday with her friend Brandon...  " + \
            "The movie they saw was called Thermal Unrest... They both wore blue " + \
            "shirts...  What day did they go to the movie?",
        "answer": "Thursday",
        "category": "memory_game"
    },
    {
        "id": 32,
        "question": "Josh bought two dozen roses for his wife Bridget on Sunday... " + \
            "Monday is their third anniversary and they're going to an italian" + \
            "restaurant called Gino's in Chicago...  How many dozen roses did Josh buy?",
        "answer": "2",
        "category": "memory_game"
    },
    {
        "id": 33,
        "question": "Justin and Tara just got back from a 9 day trip to " + \
            "Green Bay...  The trip was for a family reunion where " + \
            "they saw 31 relatives, including Tara's cousin Joey from Detroit..." + \
            " Tara hasn't seen Joey in 11 years...  What city did Justin and Tara " + \
            "just return from?",
        "answer": "Green Bay",
        "category": "memory_game"
    },
    {
        "id": 34,
        "question": "Vince traveled 1,200 miles to see his fianceé Emily " +\
            "in Seattle...  They're planning to get married next October " +\
            "in Texas... It's been 12 days since they last saw each " +\
            "other...  What is Vince's fianceé's name?'",
        "answer": "Emily",
        "category": "memory_game"
    },
    {
        "id": 35,
        "question": "Tina has three cats, Sam, Lucky, and Tips... " +\
            "Sam has white fur with patches of brown... " +\
            "Lucky is orange with long hair...  " +\
            "Tips is dark black except his ears which are white..." +\
            "What is the name of the owner of Sam, Lucky, and Tips?",
        "answer": "Tina",
        "category": "memory_game"
    },
    {
        "id": 36,
        "question": "A news article says that Florida is the number " +\
            "one place that Americans are planning to go for Summer " +\
            "vacation this year... This is caused by a reported 17% " +\
            "increase in tourism, beating out Hawaii which was last year's " +\
            "top Summer destination...  What percent increase to Florida " +\
            "tourism did the article report?",
        "answer": "17",
        "category": "memory_game"
    },
    {
        "id": 37,
        "question": "A recent study shows that teenagers who play video games " +\
            "are 38 percent more likey to pass exams with a letter grade of B or " +\
            "higher... The study hypothesizes that the mental stimulation " +\
            "enhances cognitive abilities and makes them more capable of " +\
            "problem solving and reasoning... What did the article say " +\
            "made teenagers more likely to pass exams?",
        "answer": "Video Games",
        "category": "memory_game"
    },
    {
        "id": 38,
        "question": "Julia and Mary Grace are meeting their brothers " +\
            "Patrick and Johnny for brunch... They've decided to " +\
            "go to Dove's Luncheonette in Wicker Park... How many " +\
            "people are going to brunch?",
        "answer": "4",
        "category": "memory_game"
    },
    {
        "id": 39,
        "question": "Beth is driving 2,245 miles from Port Charlotte, " +\
            "Florida to visit her daughter Katie in Phoenix, Arizona... " +\
            "The last time they saw each other was in Seattle while " +\
            "they were visiting with Beth's son Josh...  What city " +\
            "does Katie live in?",
        "answer": "Phoenix",
        "category": "memory_game"
    },
    {
        "id": 40,
        "question": "Sean and Joan are throwing an anniversary party on " +\
            "Friday for their daughter Brie and their son-in-law Ronnie... " +\
            "The party is at Del Frisco's Steakhouse located at " +\
            "9150 International Drive... What day is the party on?",
        "answer": "Friday",
        "category": "memory_game"
    },
    {
        "id": 41,
        "question": "How many strings does a violin have?",
        "answer": "4",
        "category": "simple_trivia"
    },
    {
        "id": 42,
        "question": "How many states border Florida?",
        "answer": "2",
        "category": "simple_trivia"
    },
    {
        "id": 43,
        "question": "What is a Geiger Counter used to detect?",
        "answer": "Radiation",
        "category": "simple_trivia"
    },
    {
        "id": 44,
        "question": "Babe Ruth is associated with which sport?",
        "answer": "Baseball",
        "category": "simple_trivia"
    },
    {
        "id": 45,
        "question": "What planet is the closest to Earth?",
        "answer": "Venus",
        "category": "simple_trivia"
    },
    {
        "id": 46,
        "question": "What is the total number of dots on a pair of dice?",
        "answer": "42",
        "category": "simple_trivia"
    },
    {
        "id": 47,
        "question": "How many sides does a pentagon have?",
        "answer": "5",
        "category": "simple_trivia"
    },
    {
        "id": 48,
        "question": "What is the study of fossils called?",
        "answer": "Paleontology",
        "category": "simple_trivia"
    },
    {
        "id": 49,
        "question": "Which herb is one of the main ingredients of Pesto Sauce?",
        "answer": "Basil",
        "category": "simple_trivia"
    },
    {
        "id": 50,
        "question": "Andrew Carnegie made his fortune in which industry?",
        "answer": "Steel",
        "category": "simple_trivia"
    },
    {
        "id": 51,
        "question": "The primary colors are Red... Blue... and...",
        "answer": "Yellow",
        "category": "simple_trivia"
    },
    {
        "id": 52,
        "question": "You're in a race and just overtook the person in "\
            "second place... What place are you in now?",
        "answer": "Second",
        "category": "simple_trivia"
    },
    {
        "id": 53,
        "question": "What word is associated with the words... Lock... "\
            "and... Piano...",
        "answer": "Key",
        "category": "word_association"
    },
    {
        "id": 54,
        "question": "What word is associated with the words... Ship... "\
            "and... Card...",
        "answer": "Deck",
        "category": "word_association"
    },
    {
        "id": 55,
        "question": "What word is associated with the words... Tree... "\
            "and... Car...",
        "answer": "Trunk",
        "category": "word_association"
    },
    {
        "id": 56,
        "question": "What word is associated with the words... Pillow... "\
            "and... Court...",
        "answer": "Case",
        "category": "word_association"
    },
    {
        "id": 57,
        "question": "What word is associated with the words... Bed... "\
            "and... Paper...",
        "answer": "Sheet",
        "category": "word_association"
    },
    {
        "id": 58,
        "question": "What word is associated with the words... Army... "\
            "and... Water...",
        "answer": "Tank",
        "category": "word_association"
    },
    {
        "id": 59,
        "question": "What word is associated with the words... Tennis... "\
            "and... Noise...",
        "answer": "Racket",
        "category": "word_association"
    },
    {
        "id": 60,
        "question": "What word is associated with the words... Smoker... "\
            "and... Plumber...",
        "answer": "Pipe",
        "category": "word_association"
    },
    {
        "id": 61,
        "question": "What word is associated with the words... Atomic... "\
            "and... Shell...",
        "answer": "Bomb",
        "category": "word_association"
    },
    {
        "id": 62,
        "question": "What word is associated with the words... Outer... "\
            "and... Station...",
        "answer": "Space",
        "category": "word_association"
    },
    {
        "id": 63,
        "question": "What word is associated with the words... Cruise... "\
            "and... Wreck...",
        "answer": "Ship",
        "category": "word_association"
    },
    {
        "id": 64,
        "question": "What word is associated with the words... Sphere... "\
            "and... Perfect...",
        "answer": "Circle",
        "category": "word_association"
    },
    {
        "id": 65,
        "question": "What word is associated with the words... Green... "\
            "and... Blind...",
        "answer": "Color",
        "category": "word_association"
    },
    {
        "id": 66,
        "question": "What word is associated with the words... Tone... "\
            "and... Mute...",
        "answer": "Deaf",
        "category": "word_association"
    },
    {
        "id": 67,
        "question": "Zach's 27th birthday is on July 13th... "\
            "Melissa's 26th birthday is on July 15th..." \
            "They'll celebrate both birthday's on the 17th..." \
            "How old will Melissa be?",
        "answer": "26",
        "category": "memory_game"
    },
    {
        "id": 68,
        "question": "What word can you spell with these letters:  L... I... T... T...",
        "answer": "Tilt",
        "category": "word_jumble"
    },
    {
        "id": 69,
        "question": "What word can you spell with these letters:  U... M... P... L... P...",
        "answer": "Plump",
        "category": "word_jumble"
    },
    {
        "id": 70,
        "question": "What does 3... times 1... plus 2... times 3... divided by 1... equal?",
        "answer": "15",
        "category": "simple_math"
    },
    {
        "id": 71,
        "question": "You've planned a three day trip to Seattle... " + \
            "On day one, you'll visit the Space Needle... " + \
            "On day two, you'll visit Pike Place Market..." +\
            "On day three, you'll go to Discovery Park..." +\
            "What city are you going to?",
        "answer": "Seattle",
        "category": "memory_game"
    },
    {
        "id": 72,
        "question": "How many time zones are in the continental US?",
        "answer": "4",
        "category": "simple_trivia"
    },
    {
        "id": 73,
        "question": "How many continents are there?",
        "answer": "7",
        "category": "simple_trivia"
    },
    {
        "id": 74,
        "question": "Spell the word... Friday... backwords.",
        "answer": "YADIRF",
        "category": "spelling_backwords"
    },
    {
        "id": 75,
        "question": "What word doesn't belong:  basement... ladder... steps... stairs...",
        "answer": "Basement",
        "category": "out_of_place"
    },
    {
        "id": 76,
        "question": "What word doesn't belong:  winter... cold... fall... summer...",
        "answer": "Cold",
        "category": "out_of_place"
    },
    {
        "id": 77,
        "question": "What word doesn't belong:  cookie... hamburger... pie... pudding...",
        "answer": "Hamburger",
        "category": "out_of_place"
    },
    {
        "id": 78,
        "question": "What word doesn't belong:  rain... snow... sleet... sun...",
        "answer": "Sun",
        "category": "out_of_place"
    },
    {
        "id": 79,
        "question": "What word doesn't belong:  bear... fish... cow... pig...",
        "answer": "Fish",
        "category": "out_of_place"
    },
    {
        "id": 80,
        "question": "What word doesn't belong:  lake... pond... rain... river...",
        "answer": "Rain",
        "category": "out_of_place"
    },
    {
        "id": 81,
        "question": "What word doesn't belong:  bike... window... roof... door...",
        "answer": "Bike",
        "category": "out_of_place"
    },
    {
        "id": 82,
        "question": "What word doesn't belong:  cat... dog... bird... hamster...",
        "answer": "Bird",
        "category": "out_of_place"
    },
    {
        "id": 83,
        "question": "What word doesn't belong:  apple... tomato... banana... carrot...",
        "answer": "Carrot",
        "category": "out_of_place"
    },
    {
        "id": 84,
        "question": "What word doesn't belong:  wolf... lion... buffalo... fox...",
        "answer": "Buffalo",
        "category": "out_of_place"
    },
    {
        "id": 85,
        "question": "Remember these words... Epic... Bird... Taco... Sphere... "\
            "What was the second word?",
        "answer": "Bird",
        "category": "repeat"
    },
    {
        "id": 86,
        "question": "Remember these words... Map... Computer... Fish... Blimp... "\
            "What was the first word?",
        "answer": "Map",
        "category": "repeat"
    },
    {
        "id": 87,
        "question": "Remember these words... French... Boat... Yesterday... Apple... "\
            "What was the second word?",
        "answer": "Boat",
        "category": "repeat"
    },
    {
        "id": 88,
        "question": "Remember these words... November... Star... Dream... Tuesday... "\
            "What was the last word?",
        "answer": "Tuesday",
        "category": "repeat"
    },
    {
        "id": 89,
        "question": "Remember these words... Drum... Animal... Mighty... Baron... "\
            "What was the second word?",
        "answer": "Animal",
        "category": "repeat"
    },
    {
        "id": 90,
        "question": "Remember these words... Saxophone... Analysis... War... Trumpet... "\
            "What was the third word?",
        "answer": "War",
        "category": "repeat"
    },
    {
        "id": 91,
        "question": "Remember these words... Party... Fire... Drink... Water... "\
            "What was the third word?",
        "answer": "Drink",
        "category": "repeat"
    },
    {
        "id": 92,
        "question": "Remember these words... Answer... Phone... Cancel... Shower... "\
            "What was the first word?",
        "answer": "Answer",
        "category": "repeat"
    },
    {
        "id": 93,
        "question": "Remember these words... Think... Observe... Sleep... Pizza... "\
            "What was the last word?",
        "answer": "Pizza",
        "category": "repeat"
    },
    {
        "id": 94,
        "question": "Remember these words... Pressure... Pants... Advance... Game... "\
            "What was the second word?",
        "answer": "Pants",
        "category": "repeat"
    },
    {
        "id": 95,
        "question": "Remember these words... Moment... Win... Heat... Growth... "\
            "What was the third word?",
        "answer": "Heat",
        "category": "repeat"
    },
    {
        "id": 96,
        "question": "Remember these numbers... 7... 2... 11... 4... "\
            "What was the lowest number?",
        "answer": "2",
        "category": "low_high_number"
    },
    {
        "id": 97,
        "question": "Remember these numbers... 3... 1... 9... 8... "\
            "What was the highest number?",
        "answer": "9",
        "category": "low_high_number"
    },
    {
        "id": 98,
        "question": "Remember these numbers... 12... 15... 18... 6... "\
            "What was the highest number?",
        "answer": "18",
        "category": "low_high_number"
    },
    {
        "id": 99,
        "question": "Remember these numbers... 17... 14... 15... 13... "\
            "What was the lowest number?",
        "answer": "13",
        "category": "low_high_number"
    },
    {
        "id": 100,
        "question": "Remember these numbers... 3... 8... 5... 4... "\
            "What was the lowest number?",
        "answer": "3",
        "category": "low_high_number"
    },
    {
        "id": 101,
        "question": "Remember these numbers... 13... 28... 18... 23... "\
            "What was the highest number?",
        "answer": "28",
        "category": "low_high_number"
    },
    {
        "id": 102,
        "question": "Remember these numbers... 6... 9... 5... 2... "\
            "What was the highest number?",
        "answer": "9",
        "category": "low_high_number"
    },
    {
        "id": 103,
        "question": "Remember these numbers... 37... 32... 38... 34... "\
            "What was the lowest number?",
        "answer": "32",
        "category": "low_high_number"
    },
    {
        "id": 104,
        "question": "Remember these numbers... 5... 7... 1... 3... "\
            "What was the highest number?",
        "answer": "7",
        "category": "low_high_number"
    },
    {
        "id": 105,
        "question": "Remember these numbers... 27... 22... 28... 25... "\
            "What was the lowest number?",
        "answer": "22",
        "category": "low_high_number"
    },
    {
        "id": 106,
        "question": "Remember these numbers... 13... 28... 18... 23... "\
            "What was the third number?",
        "answer": "18",
        "category": "repeat"
    },
    {
        "id": 107,
        "question": "Remember these numbers... 6... 9... 5... 2... "\
            "What was the second number?",
        "answer": "9",
        "category": "repeat"
    },
    {
        "id": 108,
        "question": "Remember these numbers... 37... 32... 38... 34... "\
            "What was the second number?",
        "answer": "32",
        "category": "repeat"
    },
    {
        "id": 109,
        "question": "Remember these numbers... 5... 7... 1... 3... "\
            "What was the third number?",
        "answer": "1",
        "category": "repeat"
    },
    {
        "id": 110,
        "question": "Remember these numbers... 27... 22... 28... 25... "\
            "What was the first number?",
        "answer": "27",
        "category": "repeat"
    }
]
