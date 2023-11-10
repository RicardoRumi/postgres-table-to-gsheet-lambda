# AWS Lambda Docker Image and ECR Deployment

This README provides instructions on how to create a Docker image for an AWS Lambda function and push it to Amazon Elastic Container Registry (ECR).

This is a simple AWS Lambda function to copy the entire contents of a PostgreSQL database table to a specified worksheet in Google Drive.

## Setting up AWS SSO and ECR Repository

1. Configure AWS SSO for the desired profile:

    ```bash
    aws configure sso --profile CREDENTIAL
    aws sso login --profile CREDENTIAL
    ```

    Follow the prompts to complete the SSO login process.

2. Create a new ECR repository to store your Lambda function's Docker image:

    ```bash
    aws ecr create-repository --repository-name lambda-google-sheets --profile CREDENTIAL
    ```

## Building the Docker Image

1. Build the Docker image locally:

    ```bash
    docker build -t my-lambda-function .
    ```

    This command builds a Docker image tagged as `my-lambda-function` from a Dockerfile in the current directory.

## Pushing the Docker Image to ECR

1. Retrieve an authentication token and authenticate your Docker client to your registry:

    ```bash
    aws ecr get-login-password --region us-east-1 --profile CREDENTIAL | docker login --username AWS --password-stdin [account-id].dkr.ecr.us-east-1.amazonaws.com
    ```

    Replace `[account-id]` with your actual AWS account ID.

2. Tag your image to match the repository's name:

    ```bash
    docker tag my-lambda-function:latest [account-id].dkr.ecr.us-east-1.amazonaws.com/lambda-google-sheets:latest
    ```

3. Push the image to AWS ECR:

    ```bash
    docker push [account-id].dkr.ecr.us-east-1.amazonaws.com/lambda-google-sheets:latest
    ```

After pushing the Docker image to ECR, it will be available for deployment as an AWS Lambda function.
