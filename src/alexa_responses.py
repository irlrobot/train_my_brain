#!/usr/bin/env python
"""
Train That Brain
v1.0.0
github.com/irlrobot/train_that_brain
"""
from __future__ import print_function

def speech(tts, attributes, end_session):
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
        "shouldEndSession": end_session
    }

def speech_with_card(tts, attributes, end_session, card_title, card_text, card_img_sm, card_img_lg):
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
                    "smallImageUrl": card_img_sm,
                    "largeImageUrl": card_img_lg
                }
            }
        },
        "shouldEndSession": end_session
    }
