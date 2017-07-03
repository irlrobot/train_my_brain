#!/usr/bin/env python
"""
Train That Brain
v1.0.0
github.com/irlrobot/train_that_brain
"""
from __future__ import print_function
from random import randint

def speech(tts, attributes, should_end_session):
    '''build speech output'''
    print("======speech fired...")
    response = {
        "version": "1.0",
        "sessionAttributes": attributes,
        "response": {
            "shouldEndSession": should_end_session,
            "outputSpeech": {
                "type": "PlainText",
                "text": tts
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

def speech_with_card(tts, attributes, should_end_session, card_title, card_text):
    '''build speech output with a card'''
    print("======speech_with_card fired...")
    response = {
        "version": "1.0",
        "sessionAttributes": attributes,
        "response": {
            "shouldEndSession": should_end_session,
            "outputSpeech": {
                "type": "PlainText",
                "text": tts
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
                    "text": "Time's up!  What's your guess?"
                }
            }
        }
    }

    print("=====response back to alexa service:  \n" + str(response))
    return response

def play_end_message():
    """play a standard message when exiting the skill"""
    standard_message = "Thanks for playing Train That Brain.  Play daily to keep "\
        "your mind muscles strong."
    review_message = "Please leave a review and let us know what you thought "\
        "of Train That Brain."

    # don't always ask for a review
    if randint(1, 3) == 1:
        tts = standard_message + " " + review_message
    else:
        tts = standard_message

    return speech(tts, {}, True)
