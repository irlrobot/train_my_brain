#!/usr/bin/env python
"""
Train My Brain
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
    if 'slots' in intent:
        answer = intent['slots'].get('CatchAllAnswer', {}).get('value').upper()
    else:
        # if we got this far we should mark it as no response because
        # another word wasn't caught by the catchcall slot (e.g. NoIntent)
        answer = "no response"
    print("=====answer heard was:  " + answer)

    game_questions = session['attributes']['questions']
    game_length = session['attributes']['game_length']
    current_score = session['attributes']['score']
    current_question_index = session['attributes']['current_question_index']
    correct_answer = game_questions[current_question_index]['answer'].upper()
    current_question = game_questions[current_question_index]['question']

    answered_correctly = None
    if correct_answer in answer:
        current_score += 10
        answered_correctly = True
    else:
        log_wrong_answer(current_question, answer, correct_answer)
        # if it's a spelling_backwords question we need
        # to add spaces into the answer so she spells it out
        if game_questions[current_question_index]['category'] == 'spelling_backwords':
            correct_answer = correct_answer.replace("", "... ")[1: -1]
        answered_correctly = False

    if current_question_index == game_length - 1:
        return end_game_return_score(current_score, attributes,
                                     answered_correctly, current_question,
                                     answer, correct_answer)

    current_question_index += 1
    speech_output = "Next question in 3... 2... 1..." +\
        game_questions[current_question_index]['question']
    attributes = {
        "current_question_index": current_question_index,
        "questions": game_questions,
        "score": current_score,
        "game_length": game_length,
        "game_status": "in_progress"
    }

    if answered_correctly:
        return speech(speech_output, attributes, should_end_session, answered_correctly)

    speech_output = "The correct answer was " + str(correct_answer) + ". " + speech_output
    card_text = "The question was:\n" + current_question + \
        "\nYou said " + answer + " but the correct answer is " + correct_answer
    return speech_with_card(speech_output, attributes, should_end_session,
                            "Here's What You Missed", card_text,
                            answered_correctly)

def end_game_return_score(current_score, attributes,
                          answered_correctly, last_question, answer,
                          correct_answer):
    """if the customer answered the last question end the game"""
    speech_output = "Brain training complete, you got  " + \
        str(current_score) + " points.  Would you like to play again?"

    if answered_correctly:
        card_text = "Your score is " + str(current_score) + " points!"
    else:
        speech_output = "The correct answer was " + str(correct_answer) +\
            ". Brain training complete, you got  " + \
            str(current_score) + " points.  Would you like to play again?"
        card_text = "Your score is " + str(current_score) + " points!\n" + \
            "\nThe last question was:\n" + last_question + \
            "\nYou said " + answer + " but the correct answer is " + correct_answer
    should_end_session = False
    attributes['game_status'] = "ended"
    return speech_with_card(speech_output, attributes, should_end_session,
                            "Results", card_text, answered_correctly)

def log_wrong_answer(question, answer, correct_answer):
    """log all questions answered incorrectly so i can analyze later"""
    print("[WRONG ANSWER]:" + question + ":" + answer + ":" + correct_answer)
