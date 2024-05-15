from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_events,
    # aws_dynamodb as dynamodb,
    aws_lambda_event_sources as event_sources,
)
from cdk_aws.iam import IAMRole
from cdk_aws.lambda_construct import LambdaFunctions
from cdk_aws.s3_construct import S3Bucket


class AwsCdkDemoStack(Stack):
    def __init__(self, scope, construct_id, deploy_env_type, config, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # S3
        self.demo_lambda_bucket = S3Bucket.create_s3_bucket(
            scope=self, 
            deploy_env_type=deploy_env_type,
            config=config
        )

        # Iam Roles
        self.demo_lambda_role = IAMRole.create_or_update_demo_lambda_role(
            scope=self,
            deploy_env_type=deploy_env_type,
            config=config
        )

        # lambdas
        self.demo_lambda = LambdaFunctions.create_or_update_demo_lambda(
            scope=self,
            deploy_env_type=deploy_env_type,
            config=config,
            iam_role=self.demo_lambda_role
        )

        LambdaFunctions.add_lambda_cron_job(
            scope=self,
            event_name="demo_lambda_cron_trigger",
            lambda_function=self.demo_lambda,
            cron_schedule=aws_events.Schedule.cron(hour="*/2", minute=0),
        )
