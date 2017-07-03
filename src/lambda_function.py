#!/usr/bin/env python
"""
Train That Brain
v1.0.0
github.com/irlrobot/train_that_brain
"""
from __future__ import print_function
import json
from play_new_game import play_new_game
from handle_answer_request import handle_answer_request
from alexa_responses import play_end_message

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
        print("=====AnswerIntent fired...")
        return handle_answer_request(intent, session)
    if intent_name == "GameIntent":
        print("=====GameIntent fired...")
        return play_new_game()
    if intent_name == "AMAZON.StartOverIntent" or "AMAZON.YesIntent":
        print("=====StartOverIntent or YesIntent fired...")
        return play_new_game()
    if intent_name == "AMAZON.StopIntent" or "AMAZON.CancelIntent" or "AMAZON.NoIntent":
        print("=====StopIntent, CancelIntent, or NoIntent fired...")
        return play_end_message()

def on_session_ended(event_request, session):
    """when the user ends the session intentionally or timeout"""
    print("=====on_session_ended requestId=" + event_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return play_end_message()
