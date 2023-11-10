import os
import boto3
import botocore
import pygsheets
import psycopg2 as pg
import pandas as pd
import logging
import json

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Hardcoded environment variables
s3_bucket = 'CREDENTIAL'
g_service_acc_key = 'CREDENTIAL'
db_hostname = 'CREDENTIAL'
db_name = 'CREDENTIAL'
db_username = 'CREDENTIAL'
db_password = 'CREDENTIAL'
db_port = CREDENTIAL
db_table = 'CREDENTIAL'
gsheet_title = 'CREDENTIAL'

def lambda_handler(event, context):
    logger.info('got event{}'.format(event))
    logger.error('something went wrong')

    # get service account key .json file from S3 and give local path
    s3 = boto3.client('s3')
    LOCAL_FILENAME = '/tmp/{}'.format(os.path.basename(g_service_acc_key))

    try:
        s3.download_file(Bucket=s3_bucket, Key=g_service_acc_key,
                         Filename=LOCAL_FILENAME)
        with open(LOCAL_FILENAME, 'r') as handle:
            parsed = json.load(handle)
            print(json.dumps(parsed, indent=4, sort_keys=True))
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

    # connect to postgres db
    conn = pg.connect(host=db_hostname,
                      dbname=db_name,
                      user=db_username,
                      password=db_password,
                      port=db_port)

    # read entire sheet into a pandas DataFrame
    df = pd.read_sql_query(f'select * from {db_table}', con=conn)

    # authorize pygsheets, open worksheet, and copy info from df to sheet
    gc = pygsheets.authorize(service_file=LOCAL_FILENAME)
    wks = gc.open(gsheet_title).sheet1
    wks.set_dataframe(df, (1, 1))

# If you are running this script directly, uncomment the following line:
# lambda_handler(None, None)
