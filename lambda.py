import json
import boto3
import os
import requests

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    download_path = '/tmp/{}'.format(key)
    s3_client.download_file(bucket, key, download_path)
    
   
    resized_image_path = call_docker_service(download_path)
    
    
    upload_path = 'resized-{}'.format(key)
    s3_client.upload_file(resized_image_path, bucket, upload_path)

    return {
        'statusCode': 200,
        'body': json.dumps('Image processed and uploaded successfully')
    }

def call_docker_service(image_path):
    
    url = 'http://your-docker-service-url/process_image'
    
    
    with open(image_path, 'rb') as image_file:
        files = {'file': image_file}
        
    
        response = requests.post(url, files=files)
        
        
        if response.status_code == 200:
            
            resized_image_path = '/tmp/resized_image.jpg'
            with open(resized_image_path, 'wb') as output_file:
                output_file.write(response.content)
            return resized_image_path
        else:
            raise Exception('Failed to process image: {}'.format(response.text))
