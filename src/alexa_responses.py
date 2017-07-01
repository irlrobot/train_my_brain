#!/usr/bin/env python
"""
Train That Brain
v1.0.0
github.com/irlrobot/train_that_brain
"""
from __future__ import print_function

def speech(tts, attributes, should_end_session):
    '''build speech output'''
    return {
        "version": "1.0",
        'sessionAttributes': attributes,
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": tts
            }
        },
        "shouldEndSession": should_end_session
    }

def speech_with_card(tts, attributes, should_end_session, card_title, card_text, image_small, image_large):
    '''build speech output with a card'''
    return {
        "version": "1.0",
        'sessionAttributes': attributes,
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": tts
            },
            "card": {
                "type": "Standard",
                "title": card_title,
                "text": card_text,
                "image": {
                    "smallImageUrl": image_small,
                    "largeImageUrl": image_large
                }
            }
        },
        "shouldEndSession": should_end_session
    }
