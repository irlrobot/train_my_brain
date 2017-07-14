#!/usr/bin/env python
"""
Train My Brain
github.com/irlrobot/train_my_brain
"""
from __future__ import print_function
from random import sample, shuffle
from alexa_responses import speech
from brain_training import QUESTIONS

def play_new_game(replay):
    """play new game intro and build question bank for the session"""
    print("=====play_new_game fired...")
    if replay:
        new_game_message = "Get ready... Starting a new game in... 3... 2... 1..."
    else:
        new_game_message = "Welcome to Train My Brain!  I'm going to give you six "\
            "brain teasers and you'll only have eight seconds to answer each one... "\
            "I won't repeat the questions so try to remember all the details...  "\
            "Starting in...  3... 2... 1..."
    questions = pick_random_questions(6)
    speech_output = new_game_message + questions[0]['question']
    should_end_session = False
    attributes = {
        "questions": questions,
        "score": 0,
        "current_question_index": 0,
        "game_length": len(questions),
        "game_status": "in_progress"
    }
    return speech(speech_output, attributes, should_end_session, None)

def pick_random_questions(num_questions):
    """pick random questions from the bank to form the game"""
    print("=====pick_random_questions fired...")
    shuffle(QUESTIONS)
    questions = sample(list(QUESTIONS), k=num_questions)

    shuffle(questions)
    return questions
