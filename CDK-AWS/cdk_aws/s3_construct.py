from aws_cdk import aws_s3 as s3

class S3Bucket:
    @staticmethod
    def create_s3_bucket(scope, deploy_env_type, config):
        # Check if the bucket already exists
        existing_bucket = s3.Bucket.from_bucket_name(scope, "ExistingBucket", config["s3_bucket_name"])

        if existing_bucket is None:
            # Create the bucket only if it doesn't already exist
            s3.Bucket(scope,
                id="s3_resource_id",
                bucket_name=config["s3_bucket_name"]
            )
