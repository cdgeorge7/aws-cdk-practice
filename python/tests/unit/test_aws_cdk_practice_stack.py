import json
import pytest

from aws_cdk import core
from aws-cdk-practice.aws_cdk_practice_stack import AwsCdkPracticeStack


def get_template():
    app = core.App()
    AwsCdkPracticeStack(app, "aws-cdk-practice")
    return json.dumps(app.synth().get_stack("aws-cdk-practice").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
