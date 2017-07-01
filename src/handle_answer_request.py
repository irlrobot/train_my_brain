#!/usr/bin/env python
"""
Train That Brain
v1.0.0
github.com/irlrobot/train_that_brain
"""
from __future__ import print_function
from alexa_responses import speech

def handle_answer_request(intent, session):
    """check if the answer is right, adjust score, and continue"""
    print("=====handle_answer_request fired...")
    attributes = {}
    should_end_session = False
    answer = intent['slots'].get('CatchAllAnswer', {}).get('value')

    game_questions = session['attributes']['questions']
    game_length = session['attributes']['game_length']
    current_score = session['attributes']['score']
    current_questions_index = session['attributes']['current_questions_index']
    correct_answer = game_questions[current_questions_index]['answer']

    answer_output = None
    if answer == correct_answer:
        current_score += 1
        answer_output = "CORRECT!"
    else:
        answer_output = "WRONG!"

    if current_questions_index == game_length:
        speech_output = answer_output + "Training complete.  You got  " + \
            current_score + " points.  Feel smarter yet?"
        should_end_session = True
        return speech(speech_output, attributes, should_end_session)

    current_questions_index += 1

    speech_output = answer_output + "Next question in 3... 2... 1..." +\
        game_questions[current_questions_index]['question']
    attributes = {
        "current_questions_index": current_questions_index,
        "questions": game_questions,
        "score": current_score,
        "game_length": game_length
    }

    return speech(speech_output, attributes, should_end_session)
