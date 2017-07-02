#!/usr/bin/env python
"""
Train That Brain
v1.0.0
github.com/irlrobot/train_that_brain
"""
from __future__ import print_function

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
            }
        }
    }
    print("=====response:  \n" + str(response))
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
                        "https://s3.amazonaws.com/aws.userdel.com/train_that_brain_small_card.jpg",
                    "largeImageUrl":
                        "https://s3.amazonaws.com/aws.userdel.com/train_that_brain_large_card.jpg"
                }
            }
        }
    }

    print("=====response:  \n" + str(response))
    return response
