import json
import boto3
import os
import logging
from datetime import datetime, timezone
# from newtools import newtools
from newtools import db
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def demo_lambda_handler(event, context):
    
    s3 = boto3.client("s3")
    
    try:
        logger.info("Function started at {}".format(datetime.now(timezone.utc)))
        bucket = os.environ.get('s3_bucket')
        print(bucket)
        key = "incoming/empty_incoming.txt"
        
        download_dir = "/tmp/"
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        
        download_path = "/tmp/{}".format(key.split('/')[-1])
        s3.download_file(bucket, key, download_path)
        
        processed_file_key = key.split('.')[0] + '_processed_file.' + key.split('.')[1]
        logger.info("Current Processing File: {}".format(processed_file_key.split('/'[-1])))
        
        output_key = 'output/{}'.format(processed_file_key.split('/')[-1])
        s3.upload_file(download_path, bucket, output_key)

        logger.info("File processed and uploaded successfully!")

        logger.info("Function Ended at {}".format(datetime.now(timezone.utc)))

    except Exception as exception_info:
        logger.error("Error Occurred", exc_info=exception_info)
        raise exception_info
