#!/usr/bin/env python
"""
Train My Brain
github.com/irlrobot/train_my_brain
"""
from __future__ import print_function
from random import randint

def speech(tts, attributes, should_end_session, answered_correctly):
    '''build speech output'''
    print("======speech fired...")
    sound = get_sound_effect_for_answer(answered_correctly)
    prompt = prompt_sound(should_end_session)
    response = {
        "version": "1.0",
        "sessionAttributes": attributes,
        "response": {
            "shouldEndSession": should_end_session,
            "outputSpeech": {
                "type": "SSML",
                "ssml": "<speak>" + sound + tts + prompt + "</speak>"
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "Time's up!  What's your guess?"
                }
            }
        }
    }
    print("=====response back to alexa service:  \n" + str(response))
    return response

def speech_with_card(tts, attributes, should_end_session, card_title,
                     card_text, answered_correctly, reprompt=None):
    '''build speech output with a card'''
    print("======speech_with_card fired...")
    sound = get_sound_effect_for_answer(answered_correctly)
    prompt = prompt_sound(should_end_session)
    if reprompt is None:
        reprompt_tts = "Time's up!  What's your guess?"
    else:
        reprompt_tts = reprompt
    response = {
        "version": "1.0",
        "sessionAttributes": attributes,
        "response": {
            "shouldEndSession": should_end_session,
            "outputSpeech": {
                "type": "SSML",
                "ssml": "<speak>" + sound + tts + prompt + "</speak>"
            },
            "card": {
                "type": "Standard",
                "title": card_title,
                "text": card_text,
                "image": {
                    "smallImageUrl":
                        "https://s3.amazonaws.com/trainthatbrain/card_small.png",
                    "largeImageUrl":
                        "https://s3.amazonaws.com/trainthatbrain/card_large.png"
                }
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": reprompt_tts
                }
            }
        }
    }

    print("=====response back to alexa service:  \n" + str(response))
    return response

def play_end_message():
    """play a standard message when exiting the skill"""
    print("=====play_end_message fired...")
    standard_message = "Thanks for playing Train My Brain!  Play daily to keep "\
        "your mind muscles strong."
    review_message = "Thanks for playing Train My Brain!  "\
        "Please leave a review and let us know what you thought."

    # don't always ask for a review
    if randint(1, 10) == 1:
        tts = review_message
    else:
        tts = standard_message

    return speech(tts, {}, True, None)

def get_sound_effect_for_answer(answer_was_right):
    """get the appropriate sound effect"""
    print("=====get_sound_effect_for_answer fired...")
    print("=====answer_was_right:  " + str(answer_was_right))
    if answer_was_right is None:
        return ""
    if answer_was_right:
        return "<audio src=\"https://s3.amazonaws.com/trainthatbrain/correct.mp3\" />"

    return "<audio src=\"https://s3.amazonaws.com/trainthatbrain/wrong.mp3\" />"

def prompt_sound(should_end_session):
    """determine if the prompt sound should play"""
    if should_end_session:
        return ''

    return "<audio src=\"https://s3.amazonaws.com/trainthatbrain/prompt.mp3\" />"
