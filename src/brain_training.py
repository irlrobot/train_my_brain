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
                "question": "What word can you spell with these letters:  S... N... W... I...",
                "answer": "Wins"
            },
            {
                "id": 2,
                "question": "What word can you spell with these letters:  O... B... I... L...",
                "answer": "Boil"
            },
            {
                "id": 3,
                "question": "What word can you spell with these letters:  E... B... U... C...",
                "answer": "Cube"
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
            }
        ]
    },
    {
        "simple_trivia": [
            {
                "id": 1,
                "question": "What is the capital of Alaska?",
                "answer": "Juneau"
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
            }
        ]
    }
]
