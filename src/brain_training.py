#!/usr/bin/env python
"""
Train That Brain
v1.0.0
github.com/irlrobot/train_that_brain
"""
QUESTIONS = [
    {
        "word_jumble": [
            {
                "id": 1,
                "question": "What word can you spell with these letters:  P... C... M... A...",
                "answer": "Camp"
            },
            {
                "id": 2,
                "question": "What word can you spell with these letters:  J... P... U... M...",
                "answer": "Jump"
            },
            {
                "id": 3,
                "question": "What word can you spell with these letters:  I... K... N... P...",
                "answer": "Pink"
            },
            {
                "id": 4,
                "question": "What word can you spell with these letters:  K... R... W... O...",
                "answer": "Work"
            },
            {
                "id": 5,
                "question": "What word can you spell with these letters:  A... S... D... F...",
                "answer": "Fads"
            },
            {
                "id": 6,
                "question": "What word can you spell with these letters:  M... R... T... I...",
                "answer": "Trim"
            },
            {
                "id": 7,
                "question": "What word can you spell with these letters:  U... L... P... P...",
                "answer": "Pulp"
            },
            {
                "id": 8,
                "question": "What word can you spell with these letters:  B... B... M... O...",
                "answer": "Bomb"
            },
            {
                "id": 9,
                "question": "What word can you spell with these letters:  I... P... E... P...",
                "answer": "Pipe"
            },
            {
                "id": 10,
                "question": "What word can you spell with these letters:  U... D... R... M...",
                "answer": "Drum"
            }
        ]
    },
    {
        "spelling_backwords": [
            {
                "id": 1,
                "question": "Spell the word... Cats... backwords.",
                "answer": "STAC"
            },
            {
                "id": 2,
                "question": "Spell the word... Puppy... backwords.",
                "answer": "YPPUP"
            },
            {
                "id": 3,
                "question": "Spell the word... Rabbit... backwords.",
                "answer": "TIBBAR"
            },
            {
                "id": 4,
                "question": "Spell the word... Blue... backwords.",
                "answer": "EULB"
            },
            {
                "id": 5,
                "question": "Spell the word... Plane... backwords.",
                "answer": "ENALP"
            },
            {
                "id": 6,
                "question": "Spell the word... Monday... backwords.",
                "answer": "YADNOM"
            },
            {
                "id": 7,
                "question": "Spell the word... Basket... backwords.",
                "answer": "TEKSAB"
            },
            {
                "id": 8,
                "question": "Spell the word... Shoe... backwords.",
                "answer": "EOHS"
            },
            {
                "id": 9,
                "question": "Spell the word... Fruit... backwords.",
                "answer": "TIURF"
            },
            {
                "id": 10,
                "question": "Spell the word... Pasta... backwords.",
                "answer": "ATSAP"
            }
        ]
    },
    {
        "simple_math": [
            {
                "id": 1,
                "question": "What does 4... plus... 8... minus... 2... equal?",
                "answer": "10"
            },
            {
                "id": 2,
                "question": "What does 3... minus... 2... minus... 3... plus... 2... equal?",
                "answer": "0"
            },
            {
                "id": 3,
                "question": "What does 10... times... 2... plus... 5... minus... 1... equal?",
                "answer": "24"
            },
            {
                "id": 4,
                "question": "What does 2... times... 8... minus... 10... minus... 1... equal?",
                "answer": "5"
            },
            {
                "id": 5,
                "question": "What does 10... plus... 50... plus... 25... minus... 7... equal?",
                "answer": "78"
            },
            {
                "id": 6,
                "question": "What does 100... minus... 42... mius 13... minus... 10... equal?",
                "answer": "35"
            },
            {
                "id": 7,
                "question": "What does 10... times... 10... minus... 9... equal?",
                "answer": "91"
            },
            {
                "id": 8,
                "question": "What does 4... plus... 9... plus... 5... times... 3... equal?",
                "answer": "54"
            },
            {
                "id": 9,
                "question": "What does 37... minus... 8... plus... 19... equal?",
                "answer": "48"
            },
            {
                "id": 10,
                "question": "What does 120... times... 2... plus... 50... minus... 11... equal?",
                "answer": "279"
            }
        ]
    },
    {
        "memory_game": [
            {
                "id": 1,
                "question": "Sara went to the movies on Thursday with her friend Brandon...  " + \
                    "The movie they saw was called Thermal Unrest... They both wore blue " + \
                    "shirts...  What day did they go to the movie?",
                "answer": "Thursday"
            },
            {
                "id": 2,
                "question": "Josh bought two dozen roses for his wife Bridget on Sunday... " + \
                    "Monday is their third anniversary and they're going to an italian" + \
                    "restaurant called Gino's in Chicago...  How many dozen roses did Josh buy?",
                "answer": "2"
            },
            {
                "id": 3,
                "question": "Justin and Tara just got back from a 9 day trip to " + \
                    "Green Bay...  The trip was for a family reunion where " + \
                    "they saw 31 relatives, including Tara's cousin Joey from Detroit..." + \
                    " Tara hasn't seen Joey in 11 years...  What city did Justin and Tara " + \
                    "just return from?",
                "answer": "Green Bay"
            },
            {
                "id": 4,
                "question": "Vince traveled 1,200 miles to see his fianceé Emily " +\
                    "in Seattle...  They're planning to get married next October " +\
                    "in Texas... It's been 12 days since they last saw each " +\
                    "other...  What is Vince's fianceé's name?'",
                "answer": "Emily"
            },
            {
                "id": 5,
                "question": "Tina has three cats, Sam, Lucky, and Tips... " +\
                    "Sam has white fur with patches of brown... " +\
                    "Lucky is orange with long hair...  " +\
                    "Tips is dark black except his ears which are white..." +\
                    "What is the name of the owner of Sam, Lucky, and Tips?",
                "answer": "Tina"
            },
            {
                "id": 6,
                "question": "A news article says that Florida is the number " +\
                    "one place that Americans are planning to go for Summer " +\
                    "vacation this year... This is caused by a reported 17% " +\
                    "increase in tourism, beating out Hawaii which was last year's " +\
                    "top Summer destination...  What percent increase to Florida " +\
                    "tourism did the article report?",
                "answer": "17"
            },
            {
                "id": 7,
                "question": "A recent study shows that teenagers who play video games " +\
                    "are 38 percent more likey to pass exams with a letter grade of B or " +\
                    "higher... The study hypothesizes that the mental stimulation " +\
                    "enhances cognitive abilities and makes them more capable of " +\
                    "problem solving and reasoning... What did the article say " +\
                    "made teenagers more likely to pass exams?",
                "answer": "Video Games"
            },
            {
                "id": 8,
                "question": "Julia and Mary Grace are meeting their brothers " +\
                    "Patrick and Johnny for brunch... They've decided to " +\
                    "go to Dove's Luncheonette in Wicker Park... How many " +\
                    "people are going to brunch?",
                "answer": "4"
            },
            {
                "id": 9,
                "question": "Beth is driving 2,245 miles from Port Charlotte, " +\
                    "Florida to visit her daughter Katie in Phoenix, Arizona... " +\
                    "The last time they saw each other was in Seattle while " +\
                    "they were visiting with Beth's son Josh...  What city " +\
                    "does Katie live in?",
                "answer": "Phoenix"
            },
            {
                "id": 10,
                "question": "Sean and Joan are throwing an anniversary party on " +\
                    "Friday for their daughter Brie and their son-in-law Ronnie... " +\
                    "The party is at Del Frisco's Steakhouse located at " +\
                    "9150 International Drive... What day is the party on?",
                "answer": "Friday"
            }
        ]
    },
    {
        "simple_trivia": [
            {
                "id": 1,
                "question": "How many strings does a violin have?",
                "answer": "4"
            },
            {
                "id": 2,
                "question": "How many states border Florida?",
                "answer": "2"
            },
            {
                "id": 3,
                "question": "What is a Geiger Counter used to detect?",
                "answer": "Radiation"
            },
            {
                "id": 4,
                "question": "Babe Ruth is associated with which sport?",
                "answer": "Baseball"
            },
            {
                "id": 5,
                "question": "What planet is the closest to Earth?",
                "answer": "Venus"
            },
            {
                "id": 6,
                "question": "What is the total number of dots on a pair of dice?",
                "answer": "42"
            },
            {
                "id": 7,
                "question": "How many sides does a pentagon have?",
                "answer": "5"
            },
            {
                "id": 8,
                "question": "What is the study of fossils called?",
                "answer": "Palaeontology"
            },
            {
                "id": 9,
                "question": "Which herb is one of the main ingredients of Pesto Sauce?",
                "answer": "Basil"
            },
            {
                "id": 10,
                "question": "Andrew Carnegie made his fortune in which industry?",
                "answer": "Steel"
            }
        ]
    }
]
