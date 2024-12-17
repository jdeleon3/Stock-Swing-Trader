from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_lambda as _lambda,
    aws_lambda_event_sources as lambda_event_sources,
    aws_ses as ses
)


class StockSwingTraderStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "StockSwingTraderQueue",
            visibility_timeout=Duration.seconds(300),
        )

        lambda_handler = _lambda.Function(self, "StockSwingTraderLambda"
                                          , runtime = _lambda.Runtime.PYTHON_3_13
                                          , handler = "predictions.handler"
                                          , code = _lambda.Code.from_asset("lambda"))
        
        lambda_event = lambda_event_sources.SqsEventSource(queue)
        

        lambda_handler.add_event_source(lambda_event)
