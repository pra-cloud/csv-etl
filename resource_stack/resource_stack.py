from aws_cdk import (
    Stack,
    aws_sqs as sqs,
    Duration,
    aws_lambda as function_lambda,
    aws_s3 as s3
)
from constructs import Construct


class ResourceStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "MyfirstBucket", versioned=True,
                           bucket_name="demo-cloud-98979867",
                           block_public_access=s3.BlockPublicAccess.BLOCK_ALL)
