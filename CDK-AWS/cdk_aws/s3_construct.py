from aws_cdk import aws_s3 as s3

class S3Bucket:
    @staticmethod
    def create_s3_bucket(scope, deploy_env_type, config):
        s3.Bucket(scope,
            id="s3_resource_id",
            bucket_name=config["s3_bucket_name"]
        )