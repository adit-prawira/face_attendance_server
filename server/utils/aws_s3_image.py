import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
load_dotenv()


class AwsS3Image:
    def __init__(self, accessKey, secretKey, bucketName, region):
        self.accessKey = accessKey
        self.secretKey = secretKey
        self.bucketName = bucketName
        self.region = region
        self.s3 = boto3.client("s3", aws_access_key_id=accessKey, aws_secret_access_key=secretKey)

    def deleteImageFromS3Bucket(self, fileName):
        try:
            print(f"Processing: Deleting {fileName} from S3 Bucket...")
            self.s3.delete_object(Bucket=self.bucketName, Key=fileName)
            print(f"Success: {fileName} has been deleted...")
        except NoCredentialsError:
            print("NoCredentialsError: Valid Credentials is not provided")

    def renameImageInS3Bucket(self, oldFile, newFile):
        try:
            print(f"Processing: Renaming {oldFile} in S3 Bucket...")
            copySource = {
                "Bucket": self.bucketName,
                "Key": oldFile
            }
            self.s3.copy_object(CopySource=copySource, Bucket=self.bucketName, Key=newFile)
            self.s3.delete_object(Bucket=self.bucketName, Key=oldFile)
            print(f"Success: {oldFile} has been renamed...")
        except NoCredentialsError:
            print("NoCredentialsError: Valid Credentials is not provided")
