import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv()

def call_claude(prompt: str) -> str:
    client = boto3.client("bedrock-runtime", region_name=os.getenv("AWS_REGION"))
    body = {
        "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
        "max_tokens": 1024,
        "temperature": 0.5,
    }

    response = client.invoke_model(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        contentType="application/json",
        accept="application/json",
        body=json.dumps(body),
    )

    result = json.loads(response["body"].read())
    return result["completion"]
