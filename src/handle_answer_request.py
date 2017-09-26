#!/usr/bin/env python
"""
Train My Brain
github.com/irlrobot/train_my_brain
"""
from __future__ import print_function
from alexa_responses import speech_with_card
from fuzzywuzzy import fuzz
from brain_training import fuzzy_match_threshold

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
    current_question_category = game_questions[current_question_index]['category']
    answered_correctly = None

    fuzzy_threshold = fuzzy_match_threshold(current_question_category)
    fuzzy_score = fuzz.partial_ratio(answer, correct_answer)

    if correct_answer in answer or fuzzy_score >= fuzzy_threshold:
        current_score += 10
        answered_correctly = True
    else:
        log_wrong_answer(current_question, answer, correct_answer)
        answered_correctly = False

    formatted_correct_answer = format_correct_answer(current_question_category,
                                                     correct_answer)

    if current_question_index == game_length - 1:
        return end_game_return_score(current_score, attributes,
                                     answered_correctly, current_question,
                                     answer, correct_answer, formatted_correct_answer)

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
        speech_output = "Correct, the answer was " + str(formatted_correct_answer) + \
            ". " + speech_output
        card_text = "The question was:\n" + current_question + \
            "\nThe answer was " + correct_answer
        card_title = "You Answered Correctly"
    else:
        speech_output = "The correct answer was " + str(formatted_correct_answer) + \
            ". " + speech_output
        card_text = "The question was:\n" + current_question + \
            "\nYou said " + answer + " but the correct answer is " + correct_answer
        card_title = "Here's What You Missed"

    return speech_with_card(speech_output, attributes, should_end_session,
                            card_title, card_text, answered_correctly)

def end_game_return_score(current_score, attributes,
                          answered_correctly, last_question, answer,
                          correct_answer, formatted_correct_answer):
    """if the customer answered the last question end the game"""
    wrap_up = "Brain training complete, you got  " + \
        str(current_score) + " points.  Would you like to play again?"

    if answered_correctly:
        speech_output = "Correct, the answer was " + str(formatted_correct_answer) + \
            ". " + wrap_up
        card_text = "Your score is " + str(current_score) + " points!\n" + \
            "The last question was: " + last_question + \
            "\nThe answer was " + correct_answer
    else:
        speech_output = "The correct answer was " + str(formatted_correct_answer) +\
            ". " + wrap_up
        card_text = "Your score is " + str(current_score) + " points!\n" + \
            "\nThe last question was: " + last_question + \
            "\nYou said " + answer + " but the correct answer is " + correct_answer
    should_end_session = False
    attributes['game_status'] = "ended"
    card_title = "Game Results"
    reprompt = "Would you like to play again?"
    return speech_with_card(speech_output, attributes, should_end_session,
                            card_title, card_text, answered_correctly, reprompt)

def log_wrong_answer(question, answer, correct_answer):
    """log all questions answered incorrectly so i can analyze later"""
    print("[WRONG ANSWER]:" + question + ":" + answer + ":" + correct_answer)

def format_correct_answer(category, correct_answer):
    """
    based on the category we may need to format the correct answer
    so she repeats it back a little slower or spells it out
    """
    # if it's a spelling_backwords question we need
    # to add spaces into the answer so she spells it out
    if category == 'spelling_backwords':
        return correct_answer.replace("", "... ")[1: -1]
    # if it's repeat add elipses to slow down her saying it back
    if category == 'repeat':
        return correct_answer.replace(" ", "... ")

    return correct_answer
