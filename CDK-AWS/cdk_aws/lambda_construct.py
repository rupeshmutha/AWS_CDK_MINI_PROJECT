"""Demo lambda function"""

from aws_cdk import Duration, aws_lambda as _lambda, aws_events, Size, aws_events_targets as targets
from aws_cdk.aws_lambda import Function


class LambdaFunctions:
    """Create Lambda functions required by Brand effect's Kinetiq Ad Ingest application."""

    @staticmethod
    def create_or_update_demo_lambda(
        scope, deploy_env_type, config, iam_role, logger_layer
    ) -> Function:
        demo_lambda_handler = _lambda.Function(
            scope,
            id="demo_lambda_resource_id",
            code=_lambda.Code.from_asset("../CDK-AWS/lambda_codes/"),
            handler="demo_lambda_module.demo_lambda_handler",
            runtime=_lambda.Runtime("python3.10"),
            function_name="demo_lambda_{}".format(deploy_env_type),
            role=iam_role,
            timeout=Duration.minutes(5),
            layers=[logger_layer],
            architecture=_lambda.Architecture.X86_64,
            environment={
                "APPLICATION_NAME": config["aws_cdk_demo_lambda"],
                "s3_bucket" : config["s3_bucket_name"]
            },
        )
        return demo_lambda_handler
    
    @staticmethod
    def add_lambda_cron_job(
            scope,
            event_name: str,
            lambda_function: _lambda.Function,
            cron_schedule: aws_events.Schedule
    ) -> None:
        """Method to add a cron schedule to a lambda function."""
        event_rule = aws_events.Rule(
            scope=scope,
            id=event_name,
            schedule=cron_schedule
        )
        event_rule.add_target(target=targets.LambdaFunction(lambda_function))