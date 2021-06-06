
"""
**S3 bucket details:**  Public access
**Region:**             eu-west-1
**Bucket:**             discovery-insure-interview-rev1.
"""

import boto3
import botocore
from botocore import UNSIGNED
from botocore.config import Config
from botocore.handlers import disable_signing

BUCKET_NAME = "discovery-insure-interview-rev1"


def get_s3_bucket(bucket_name=BUCKET_NAME):
    print("Connection to S3 Bucket")
    resource = boto3.resource('s3')
    resource.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)
    my_bucket = resource.Bucket(bucket_name)
    return my_bucket


def print_file_from_s3_bucket(s3_bucket=None):
    print("Printing S3 Bucket files.")

    try:
        if s3_bucket is None:
            s3_bucket = get_s3_bucket()
        all_files = s3_bucket.objects.all()
        for file in all_files:
            print(file.key)

    except Exception as error:
        print(error)


def download_files(s3_bucket=None):
    print("Downloading S3 Bucket files.")
    resource = boto3.resource('s3')
    resource.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)
    if s3_bucket is None:
        s3_bucket = get_s3_bucket()

    for my_bucket_object in s3_bucket.objects.all():

        output_file = my_bucket_object.key.split('/')[-1].strip()
        print(f"Downloading file {output_file}")
        if output_file == "challenge3/":
            continue
        resource.Object(my_bucket_object.bucket_name, my_bucket_object.key).download_file(f'C:\\Users\\PC\\PycharmProjects\\telematics\\challenge 3\\aws\\challenge3\\{output_file}')

    print("")


my_bucket = get_s3_bucket()
print_file_from_s3_bucket(my_bucket)
download_files(my_bucket)

