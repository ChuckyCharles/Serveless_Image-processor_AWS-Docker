terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.58"
    }
  }
}

provider "aws" {
  region = "us-east-1" 
}

resource "aws_lambda_function" "dev_lam" {
  function_name = "dev_lam"
  filename      = "/home/charles/dev_lam.ipynb"  
  role          = aws_iam_role.lambda_role.arn
  handler       = "lambda_function.lambda_handler"  
  runtime       = "python3.12"

  source_code_hash = filebase64sha256("/home/charles/dev_lam.ipynb")   
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda-role-dev-lam"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect    = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        },
        Action    = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy_attachment" "s3_readonly_access" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
}

