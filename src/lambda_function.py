#!/usr/bin/env python
"""
Train My Brain
An Alexa Skill by Josh Campbell
"""
import json
import logging
from play_new_game import play_new_game
from handle_answer_request import handle_answer_request
from alexa_responses import play_end_message, speech

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def lambda_handler(event, _context):
    """AWS Lambda Entry Point"""
    logger.debug('=====lambda handler started...')
    logger.debug(json.dumps(event))
    logger.info("Request ID: {}\nSession: {}".format(
            event['request']['requestId'], event['session']))

    # If a one-shot was used to start a new game
    if event['session']['new'] and event['request']['type'] == "IntentRequest":
        return play_new_game(replay=False)
    if event['request']['type'] == "LaunchRequest":
        return play_new_game(replay=False)
    if event['request']['type'] == "IntentRequest":
        return on_intent(event['request']['intent'], event['session'])
    if event['request']['type'] == "SessionEndedRequest":
        return play_end_message()

    # todo politely bug out and log a crash dump if we hit none of the above
    
def on_intent(intent, session):
    """Router for all IntentRequest's"""
    intent_name = intent['name']
    logger.debug("=====IntentRequest: " + intent_name)

    if intent_name == "AnswerIntent":
        logger.debug("=====AnswerIntent fired...")
        if 'attributes' in session and 'questions' in session['attributes']:
            return handle_answer_request(intent, session)

        # We probably got here because the user said something other than
        # yes or no after asking if they wanted to play the game again.
        logger.info("=====No attributes in session, ending game!")
        return play_end_message()

    if intent_name == "GameIntent":
        logger.debug("=====GameIntent fired...")
        # If there's a session and we're in a game, treat this as an answer.
        # Unfortunately it will be wrong but it's better than starting over.
        if 'attributes' in session and\
            session['attributes']['game_status'] == "in_progress":
                return handle_answer_request(intent, session)
        return play_new_game(replay=False)

    if intent_name in ("AMAZON.StartOverIntent", "AMAZON.YesIntent"):
        logger.debug("=====StartOverIntent or YesIntent fired, new game...")
        return play_new_game(replay=True)

    if intent_name == "AMAZON.NoIntent":
        logger.debug("=====NoIntent fired...")
        # If there's a session and we're in a game treat this as a wrong answer
        if 'attributes' in session:
            if session['attributes']['game_status'] == "in_progress":
                return handle_answer_request(intent, session)
        # Otherwise end the game
        return play_end_message()

    if intent_name in ("AMAZON.StopIntent", "AMAZON.CancelIntent"):
        logger.debug("=====StopIntent or CancelIntent fired...")
        return play_end_message()

    if intent_name == "AMAZON.HelpIntent":
        logger.debug("=====HelpIntent fired...")
        tts = "During the game I'll give you 6 random brain teasers and only 8 "\
            "seconds to anser each one... To make your mind muscles stronger, I "\
            "won't repeat any of the questions, so try to remember all the "\
            "details... You can say 'Start Over' if you'd like a new game, "\
            "or make your guess for the last question..."
        return speech(tts, session['attributes'], 
            should_end_session=False, answered_correctly=None)
