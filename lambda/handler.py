import json
import boto3

rekognition = boto3.client('rekognition')

def lambda_handler(event, context):
    print("EVENT:", json.dumps(event))

    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']

    # Extract employee ID from filename (emp001.jpg)
    filename = key.split('/')[-1]
    employee_id = filename.split('.')[0]

    # Rekognition call (example)
    response = rekognition.detect_faces(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': key
            }
        },
        Attributes=['DEFAULT']
    )

    print(f"Attendance marked for {employee_id}")

    return {
        'statusCode': 200,
        'body': f"Attendance marked for {employee_id}"
    }
