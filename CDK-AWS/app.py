from configparser import ConfigParser, ExtendedInterpolation
import aws_cdk as cdk
from cdk_aws.cdk_aws_stack import AwsCdkDemoStack

def cdk_app():
    env_config = ConfigParser(interpolation=ExtendedInterpolation())
    env_config.read("config/demo_config.ini")

    app = cdk.App()

    # fetch deployment related configuration
    deploy_env_type = app.node.try_get_context("env").lower()
    # deploy_account = app.node.try_get_context("account").lower()
    deploy_region = app.node.try_get_context("region").lower()
    
    deploy_param ={
        # ACCOUNT_ID:deploy_account,
        "region":deploy_region,
    }
    deploy_env_conf = dict(env_config[deploy_env_type])
    global_env_conf = dict(env_config['global'])
    env_conf = {**deploy_env_conf, **global_env_conf, **deploy_param}

    env = cdk.Environment(
        # account=env_conf.get(ACCOUNT_ID),
        region=env_conf.get("region"),
    )

    # instantiate Kinetiq Ingest Main Stack
    stack_name =  "AwsCdkDemoStack" if deploy_env_type.lower() == "prod" else "aws-cdk-demo-stack-{env}".format(env=deploy_env_type.replace("_", "-"))
    AwsCdkDemoStack(app, stack_name, deploy_env_type, env_conf, env=env)

    app.synth()

if __name__ == "__main__":
    cdk_app()