#!/usr/bin/env python3

from aws_cdk import core

from hybrid.hybrid_stack import HybridStack


app = core.App()
HybridStack(app, "hybrid")

app.synth()
