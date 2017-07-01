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

def on_launch(launch_request, session):
    """when customer launches the skill via modal"""
    print("=====on_launch requestId:  " + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return play_new_game()

def on_intent(intent_request, session):
    """when customer launches the skill via modal"""
    print("=====on_intent requestId:  " + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    if intent_name == "AnswerIntent":
        return handle_answer_request(intent, session)
    if intent_name == "GameIntent":
        return play_new_game()

def on_session_ended(session_ended_request, session):
    """
    Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("=====on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
