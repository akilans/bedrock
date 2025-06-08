import boto3
import json

bedrock = boto3.client("bedrock")

models= bedrock.list_foundation_models()

print(json.dumps(models,indent=4))