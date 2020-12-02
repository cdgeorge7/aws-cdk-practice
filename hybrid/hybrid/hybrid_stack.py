from aws_cdk import (core,
                     aws_lambda as _lambda,
                     aws_apigateway as apigw,
                     aws_apigatewayv2 as apigw2,
                     aws_apigatewayv2_integrations as integrations)


class HybridStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # The code that defines your stack goes here
        # Sorry, it's late
        toots_function = _lambda.Function(self, "Toots Function", runtime=_lambda.Runtime.NODEJS_12_X,
                                          code=_lambda.Code.asset('lambda'), handler="index.handler")
        apigw.LambdaRestApi(
            self, 'Endpoint', handler=toots_function)
        # Couldn't get http api working...documentation for python is really bad, probably just going to stick with SAM
        # messageIntegration = integrations.LambdaProxyIntegration(handler=toots_function)
        # httpApi = apigw2.HttpApi(self, 'HttpApi')
        # httpApi.add_routes(path="message",methods=[apigw2.HttpMethod.GET], integration=messageIntegration)
