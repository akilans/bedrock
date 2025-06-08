import boto3
import json

client = boto3.client('bedrock-runtime')
history = []

def get_history():
    return "\n".join(history)

def generate_config():
    body_content = json.dumps({
        "inputText": get_history(),
        "textGenerationConfig":
        {
            "maxTokenCount": 8192,
            "stopSequences": [],
            "temperature": 0,
            "topP": 1
        }
    })
    return body_content

print("Bot: I'm your Bot. Ask me anything!!!")
while True:
    user_input = input("User: ")
    history.append("User: " + user_input)
    if (user_input == "exit"):
        break
    response = client.invoke_model(
        body=generate_config(),
        contentType='application/json',
        accept='application/json',
        modelId='amazon.titan-text-express-v1',
    )
    response_body = json.loads(response.get("body").read())
    bot_answer = response_body["results"][0]["outputText"].strip()
    print(bot_answer)
    history.append(bot_answer)