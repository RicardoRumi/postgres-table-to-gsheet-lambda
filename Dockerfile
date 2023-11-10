# Define your base image
FROM public.ecr.aws/lambda/python:3.10

# Copy your requirements file
COPY requirements.txt .

# Install the function's dependencies using the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code
COPY app.py .

# You can also set environment variables in the Dockerfile (or use a .env file)
# S3_CONFIG_FILE_KEY is the name of the json file that you downloaded from GCP
ENV S3_BUCKET_NAME=CREDENTIAL \
    S3_CONFIG_FILE_KEY=CREDENTIAL \
    DB_HOSTNAME=CREDENTIAL \
    DB_NAME=CREDENTIAL \
    DB_USERNAME=CREDENTIAL \
    DB_PASSWORD=CREDENTIAL \
    DB_PORT=CREDENTIAL \
    DB_TABLE_NAME=CREDENTIAL \
    GSHEET_TITLE=CREDENTIAL


# Set the CMD to your handler
CMD ["app.lambda_handler"]
