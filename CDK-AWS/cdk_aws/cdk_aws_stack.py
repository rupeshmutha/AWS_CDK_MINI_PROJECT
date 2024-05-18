from aws_cdk import (
    Stack,
    aws_events    
)
from cdk_aws.iam_construct import IAMRole
from cdk_aws.lambda_construct import LambdaFunctions
from cdk_aws.layer_construct import LambdaLayer

class AwsCdkDemoStack(Stack):
    def __init__(self, scope, construct_id, deploy_env_type, config, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Iam Roles
        self.demo_lambda_role = IAMRole.create_or_update_demo_lambda_role(
            scope=self,
            deploy_env_type=deploy_env_type,
            config=config
        )
        
        #Layer
        self.kinetiq_ingest_application_layer = LambdaLayer.create_or_update_application_layer(
            scope=self, 
            deploy_env_type=deploy_env_type
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
            cron_schedule=aws_events.Schedule.cron(minute="0/15")
        )
