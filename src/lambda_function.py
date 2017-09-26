#!/usr/bin/env python
"""
Train My Brain
github.com/irlrobot/train_my_brain
"""
from __future__ import print_function
import json
from play_new_game import play_new_game
from handle_answer_request import handle_answer_request
from alexa_responses import play_end_message, speech

def lambda_handler(event, _context):
    """main function for AWS Lambda"""
    print('=====lambda handler started...')
    print(json.dumps(event))

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])
        # this will trigger if a one shot is used
        if event['request']['type'] == "IntentRequest":
            return on_launch(event['request'], event['session'])

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
    return play_new_game(False)

def on_intent(event_request, session):
    """when customer launches the skill via modal"""
    print("=====on_intent requestId:  " + event_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = event_request['intent']
    intent_name = event_request['intent']['name']
    print("=====intent is: " + intent_name)

    if intent_name == "AnswerIntent":
        print("=====AnswerIntent fired...")
        if 'attributes' in session:
            if 'questions' in session['attributes']:
                return handle_answer_request(intent, session)

        # we probably got here because user said something other than
        # yes or no after asking if they wanted to play the game again
        print("=====no attributes ending game")
        return play_end_message()
    if intent_name == "GameIntent":
        print("=====GameIntent fired...")
        # if there's a session and we're in a game treat this as an answer
        # unfortunately it will be wrong but it's better than starting over
        if 'attributes' in session:
            if session['attributes']['game_status'] == "in_progress":
                return handle_answer_request(intent, session)
        return play_new_game(False)
    if intent_name in ("AMAZON.StartOverIntent", "AMAZON.YesIntent"):
        print("=====StartOverIntent or YesIntent fired...")
        return play_new_game(True)
    if intent_name == "AMAZON.NoIntent":
        print("=====NoIntent fired...")
        # if there's a session and we're in a game treat this as a wrong answer
        if 'attributes' in session:
            if session['attributes']['game_status'] == "in_progress":
                return handle_answer_request(intent, session)
        # otherwise end the game
        return play_end_message()
    if intent_name in ("AMAZON.StopIntent", "AMAZON.CancelIntent"):
        print("=====StopIntent or CancelIntent fired")
        return play_end_message()
    if intent_name == 'AMAZON.HelpIntent':
        print("=====HelpIntent...")
        tts = "During the game I'll give you 6 random brain teasers and only 8 "\
            "seconds to anser each one... To make your mind muscles stronger, I "\
            "won't repeat any of the questions, so try to remember all the "\
            "details... You can say 'Start Over' if you'd like a new game, "\
            "or make your guess for the last question..."
        return speech(tts, session['attributes'], False, None)

def on_session_ended(event_request, session):
    """when the user ends the session intentionally or timeout"""
    print("=====on_session_ended requestId=" + event_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return play_end_message()
