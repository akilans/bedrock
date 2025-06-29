import boto3
import json
import base64
import threading
import sys
import time
import itertools

client = boto3.client('bedrock-runtime')

# loading icons
def emoji_spinner():
    emojis = ['🖼️', '🌀', '✨', '🎨', '🧠', '🔄']
    for c in itertools.cycle(emojis):
        if done:
            break
        sys.stdout.write(f'\rSit back, I\'m generating images... {c}')
        sys.stdout.flush()
        time.sleep(0.3)
    sys.stdout.write('\r✅ Images generated successfully!        \n')


# create payload
def get_configuration(query):
    return json.dumps({
        "taskType": "TEXT_IMAGE",
        "textToImageParams": {
            "text": query
        },
        "imageGenerationConfig": {
            "quality": "standard",
            "numberOfImages": 2,
            "height": 1024,
            "width": 1024
        }
    })


# invoke model and save the images
def generate_image(user_input):
    response = client.invoke_model(
        body=get_configuration(user_input),
        contentType='application/json',
        accept='application/json',
        modelId='amazon.titan-image-generator-v1',
    )

    response_body = json.loads(response.get("body").read())
    base64_encoded_images = response_body.get("images")
    print("\n")
    for index, base64_encoded_image in enumerate(base64_encoded_images):
        binary_image = base64.b64decode(base64_encoded_image.encode('ascii'))
        filename = f"image_{index+1}.png"
        with open(filename, "wb") as f:
            f.write(binary_image)
            print(f"generated image - {filename}")


# Main program
if __name__ == "__main__":
    print("Bot: I'm your Bot. Ask me to generate any image!!!")
    user_input = input("User: ")

    done = False
    t = threading.Thread(target=emoji_spinner)
    t.start()

    generate_image(user_input)

    done = True
    t.join()