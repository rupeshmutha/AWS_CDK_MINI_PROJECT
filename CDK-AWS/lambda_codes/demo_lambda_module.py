def demo_lambda_handler(event, context):
    
    try:
        print("CDK Tested Successfully")
    except Exception as exception_info:
        return exception_info
    