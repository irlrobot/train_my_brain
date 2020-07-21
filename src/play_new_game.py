#!/usr/bin/env python
"""
Train My Brain
github.com/irlrobot/train_my_brain
"""
import logging
from random import sample, shuffle
from alexa_responses import speech
from brain_training import QUESTIONS

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def play_new_game(replay):
    """play new game intro and build question bank for the session"""
    logger.debug("=====play_new_game fired...")
    if replay:
        new_game_message = """
        <amazon:emotion name="excited" intensity="medium">
        Get ready!
        </amazon:emotion>
        Starting the game in:
        3 <break time="1s"/>
        2 <break time="1s"/>
        1 <break time="1s"/>
        """
    else:
        new_game_message = """
        <amazon:emotion name="excited" intensity="medium">
        Welcome to Train My Brain!
        </amazon:emotion>
        I'm going to give you six brain teasers and you'll only have eight 
        seconds to answer each one.
        <break time="400ms"/>
        I won't repeat the questions so try to remember all the details.
        <break time="400ms"/>
        Starting the game in:
        3 <break time="1s"/>
        2 <break time="1s"/>
        1 <break time="1s"/>
        """
    questions = pick_random_questions(6)
    speech_output = new_game_message + questions[0]['question']
    should_end_session = False
    attributes = {
        "questions": questions,
        "score": 0,
        "current_question_index": 0,
        "game_length": len(questions),
        "game_status": "in_progress"
    }
    return speech(speech_output, attributes, should_end_session, None)


def pick_random_questions(num_questions):
    """pick random questions from the bank to form the game"""
    logger.debug("=====pick_random_questions fired...")
    shuffle(QUESTIONS)
    questions = sample(list(QUESTIONS), k=num_questions)

    shuffle(questions)
    return questions
