from aws_cdk import aws_lambda as _lambda


class LambdaLayer:
    """This class is responsible for creating lambda layers required by Stack"""

    @staticmethod
    def create_or_update_application_layer(scope, deploy_env_type):
        lambda_layer= _lambda.LayerVersion(
            scope,
            id="logger_layer_resource_id",
            code=_lambda.AssetCode("../CDK-AWS/lambda_layers/"),
            layer_version_name="demo_lambda_logging_layer_{}".format(deploy_env_type),
            compatible_runtimes=[_lambda.Runtime("python3.10")],
            compatible_architectures=[_lambda.Architecture.ARM_64]
        )
        return lambda_layer