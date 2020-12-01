#!/usr/bin/env python3

from aws_cdk import core

from aws_cdk_practice.aws_cdk_practice_stack import AwsCdkPracticeStack


app = core.App()
AwsCdkPracticeStack(app, "aws-cdk-practice", env={'region': 'us-east-2'})

app.synth()
