# Serveless_Image-processor_AWS-Docke

![docker_serverless](https://github.com/user-attachments/assets/3c42853c-c334-4336-a60a-e892fa670089)


The project utilises. s3, lambda function, ECR and ECS.

An image is uploaded to the AWS s3. 

#The s3 put event triggers the lamda fucntion which retrieves the image metadata (size)

The lamda function docker invokes the docker container to process the image.

#The conatiner processes the image (re-sizing it ) and outputs the processed image to the function.

The kambda function temporarily stores the image and later uploads it to another s3 bucket.






