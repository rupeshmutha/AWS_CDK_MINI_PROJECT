from aws_cdk import aws_iam as iam


class IAMRole:
    """This class is responsible for creating IAM roles required by Stack.
        Below are the list of roles
            1. demo_lambda_role
    """
    
    @staticmethod
    def create_or_update_demo_lambda_role(scope, deploy_env_type, config):
        """iam role related to demo lambda function"""
        demo_lambda_role = iam.Role(
            scope,
            id="demo_lambda_role",
            role_name="demo_lambda_role",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        )
        demo_lambda_role.attach_inline_policy(
            iam.Policy(
                scope, id="demo_lambda_s3_access_resource_id",
                policy_name="s3_bucket_access_policy",
                statements= [
                    iam.PolicyStatement(
                        effect=iam.Effect.ALLOW,
                        actions= [
                            "s3:PutObject",
                            "s3:GetObject",
                            "s3:ListBucket"
                        ],
                        resources= [
                            f"arn:aws:s3:::{config['s3_bucket_name']}",
                            f"arn:aws:s3:::{config['s3_bucket_name']}/*"
                        ]
                    )
                ],
            )
        )
        demo_lambda_role.attach_inline_policy(
            iam.Policy(
                scope, id="demo_lambda_cloudwatch_access_resource_id",
                policy_name="cloudwatch_bucket_access_policy",
                statements=[
                    iam.PolicyStatement(
                        effect=iam.Effect.ALLOW,
                        actions=[
                            "logs:CreateLogGroup",
                            "logs:CreateLogStream",
                            "logs:PutLogEvents",
                            "cloudwatch:PutMetricData"
                        ],
                        resources=[
                            "*"
                        ]
                    )
                ]
            )
        )
        return demo_lambda_role