#!/usr/bin/env python
"""
Bundle and deploy the Lambda function
v1.0.0
"""
import logging
import shutil
import sys
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def publish_new_version(artifact, func_name):
    """
    Publishes new version of the AWS Lambda Function
    """
    try:
        session = boto3.Session(profile_name='perfect4alexa')
        client = session.client('lambda', region_name='us-east-1')
    except ClientError as err:
        logger.error("Failed to create boto3 client.\n" + str(err))
        return False

    try:
        response = client.update_function_code(
            FunctionName=str(func_name),
            ZipFile=open(artifact, 'rb').read(),
            Publish=False
        )
        logger.info(response)
        return response
    except ClientError as err:
        logger.error("Failed to update function code.\n" + str(err))
        return False
    except IOError as err:
        logger.error("Failed to access " + artifact + ".\n" + str(err))
        return False

def main():
    " Your favorite wrapper's favorite wrapper "
    logger.debug("Creating deployment package...")
    shutil.make_archive("lambda_function", "zip", "src")

    logger.debug("Starting deploy...")
    published_new_version = publish_new_version(
        "../lambda_function.zip", "train_my_brain")

    if published_new_version:
        logger.debug("New version successfully published!")
        sys.exit(0)
    else:
        logger.debug("Failed to deploy!")
        sys.exit(1)

if __name__ == "__main__":
    main()