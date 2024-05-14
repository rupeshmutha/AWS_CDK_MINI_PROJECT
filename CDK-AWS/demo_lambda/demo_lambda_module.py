import boto3
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        bucket = os.environ.get('s3_bucket')
        # bucket = event['Records'][0]['s3']['bucket']['name']
        print(bucket)
        key = event['Records'][0]['s3']['object']['key']
        print(key)
        
        # Download the file from S3
        download_path = '/tmp/{}'.format(key)
        s3.download_file(bucket, key, download_path)
        
        # Add suffix to the file name
        processed_file_key = key.split('.')[0] + '_processed_file.' + key.split('.')[1]
        
        # Upload the processed file to S3
        output_bucket = 'demo_lambda_bucket'
        output_key = 'output/{}'.format(processed_file_key)
        s3.upload_file(download_path, output_bucket, output_key)
        return {
        'statusCode': 200,
        'body': 'File processed and uploaded successfully!'
            }
    except Exception as e:
        print(e)
    