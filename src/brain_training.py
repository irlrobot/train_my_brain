#!/usr/bin/env python
"""
Train My Brain
v1.0.0
github.com/irlrobot/train_that_brain
"""
"""
Categories:
1. word_jumble
2. spelling_backwords
3. simple_math
4. memory_game
5. simple_trivia
"""
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
        "question": "Spell the word... Blue... backwords.",
        "answer": "EULB",
        "category": "spelling_backwords"
    },
    {
        "id": 15,
        "question": "Spell the word... Plane... backwords.",
        "answer": "ENALP",
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
    }
]
