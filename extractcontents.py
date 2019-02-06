import boto3
import botocore
import os

session = boto3.Session(profile_name='default') #use awscli tocreate a profile giving access and secret keys of aws
s3 = boto3.resource('s3')
BUCKET_NAME = s3.Bucket('mybucketname') # replace with your bucket name

try:
    for object in BUCKET_NAME.objects.all():    #extract all contents of a s3 bucket
        path, filename = os.path.split(object.key)
        BUCKET_NAME.download_file(object.key, filename)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
