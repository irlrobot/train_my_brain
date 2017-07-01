#!/usr/bin/env python
"""
Train That Brain
v1.0.0
github.com/irlrobot/train_that_brain
"""
from __future__ import print_function
from alexa_responses import speech, speech_with_card

def handle_answer_request(intent, session):
    """check if the answer is right, adjust score, and continue"""
    print("=====handle_answer_request fired...")
    attributes = {}
    should_end_session = False
    answer = intent['slots'].get('CatchAllAnswer', {}).get('value')
    print("=====answer heard was:  " + answer)

    game_questions = session['attributes']['questions']
    game_length = session['attributes']['game_length']
    current_score = session['attributes']['score']
    current_question_index = session['attributes']['current_question_index']
    correct_answer = game_questions[current_question_index]['answer']
    current_question = game_questions[current_question_index]['question']

    answer_output = None
    answered_correctly = None
    if answer == correct_answer:
        current_score += 1
        answer_output = "CORRECT!"
        answered_correctly = True
    else:
        log_wrong_answer(current_question, answer, correct_answer)
        answer_output = "WRONG!"
        answered_correctly = False

    if current_question_index == game_length - 1:
        return end_game_return_score(answer_output, current_score, attributes,
                                     answered_correctly, current_question, answer, correct_answer)

    current_question_index += 1
    speech_output = answer_output + "Next question in 3... 2... 1..." +\
        game_questions[current_question_index]['question']
    attributes = {
        "current_question_index": current_question_index,
        "questions": game_questions,
        "score": current_score,
        "game_length": game_length
    }

    if answered_correctly:
        return speech(speech_output, attributes, should_end_session)

    card_text = "The question was:\n" + current_question + \
        "\nYou said " + answer + " but the correct answer is " + correct_answer
    return speech_with_card(speech_output, attributes, should_end_session,
                            "Here's What You Missed", card_text)

def end_game_return_score(answer_output, current_score, attributes,
                          answered_correctly, last_question, answer, correct_answer):
    """if the customer answered the last question end the game"""
    speech_output = answer_output + "Brain Training complete.  You got  " + \
        str(current_score) + " points.  Feel smarter yet?"
    if answered_correctly:
        card_text = "Your score is " + str(current_score) + " points!"
    else:
        card_text = "Your score is " + str(current_score) + " points!\n" + \
            "\nThe last question was:\n" + last_question + \
            "\nYou said " + answer + " but the correct answer is " + correct_answer
    should_end_session = True
    return speech_with_card(speech_output, attributes, should_end_session,
                            "Results", card_text)

def log_wrong_answer(question, answer, correct_answer):
    """log all questions answered incorrectly so i can analyze later"""
    print("[WRONG ANSWER]:" + question + ":" + answer + ":" + correct_answer)
