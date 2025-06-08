import boto3
import json

client = boto3.client('bedrock-runtime')

body_content = json.dumps({
    "prompt": "What is the oldest language still spoken",
    "max_gen_len": 4000,
    "temperature": 0,
    "top_p": 0.9
})

response = client.invoke_model(
    body=body_content,
    contentType='application/json',
    accept='application/json',
    modelId='us.meta.llama3-1-70b-instruct-v1:0',
)


response_body = json.loads(response.get("body").read())

with open("result.json","w") as f:
    json.dump(response_body,f,indent=4)