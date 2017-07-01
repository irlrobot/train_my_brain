#!/usr/bin/env python
"""
Train That Brain
v1.0.0
github.com/irlrobot/train_that_brain
"""
from __future__ import print_function
import random
from alexa_responses import speech
from brain_training import QUESTIONS

def play_new_game():
    """play new game intro and build question bank for the session"""
    new_game_message = "Welcome to Train That Brain!  I'll give you ten "\
    "questions within about sixty seconds for you to answer.  Answer "\
    "as fast as you can.  Starting in...  3... 2... 1..."
    questions = pick_random_questions(2, 2)
    speech_output = new_game_message + questions[0]['question']
    should_end_session = False
    attributes = {
        "questions": questions,
        "score": 0,
        "current_question_index": 0
    }
    return speech(speech_output, attributes, should_end_session)

def pick_random_questions(num_categories, num_questions):
    """pick random questions from the bank to form the game"""
    categories = random.sample(list(QUESTIONS), k=num_categories)
    questions = []
    for category in categories:
        category_name = next(iter(category))
        category_questions = random.sample(list(category[category_name]), k=num_questions)
        for category_question in category_questions:
            questions.append(category_question)

    return questions
