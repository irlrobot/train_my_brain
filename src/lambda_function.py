#!/usr/bin/env python
"""
Train That Brain
v1.0.0
github.com/irlrobot/train_that_brain
"""
from __future__ import print_function
import json
from random import randint
from play_new_game import play_new_game
from handle_answer_request import handle_answer_request
from alexa_responses import speech

def lambda_handler(event, _context):
    """main function for AWS Lambda"""
    print('=====lambda handler started...')
    print(json.dumps(event))

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    if event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    if event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

def on_session_started(session_started_request, session):
    """when starting a new session"""
    print("=====on_session_started requestId:  " +
          session_started_request['requestId'] + ", sessionId=" +
          session['sessionId'])

def on_launch(event_request, session):
    """when customer launches the skill via modal"""
    print("=====on_launch requestId:  " + event_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return play_new_game()

def on_intent(event_request, session):
    """when customer launches the skill via modal"""
    print("=====on_intent requestId:  " + event_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = event_request['intent']
    intent_name = event_request['intent']['name']

    if intent_name == "AnswerIntent":
        return handle_answer_request(intent, session)
    if intent_name == "GameIntent":
        return play_new_game()
    if intent_name == "AMAZON.StopIntent" or "AMAZON.CancelIntent":
        tts = "Thanks for playing.  Please leave a review and let us know what you thought."
        return speech(tts, {}, True)

def on_session_ended(event_request, session):
    """when the user ends the session intentionally or timeout"""
    print("=====on_session_ended requestId=" + event_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    standard_message = "Thanks for playing Train That Brain."
    review_message = "Please leave a review and let us know what you thought "\
        "of Train That Brain."

    # don't always ask for a review
    if randint(1, 2) == 1:
        tts = standard_message + review_message
    else:
        tts = standard_message

    return speech(tts, {}, True)
