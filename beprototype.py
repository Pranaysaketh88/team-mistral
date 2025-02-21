import requests
import json

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer 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",
        "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional
        "X-Title": "<YOUR_SITE_NAME>",  # Optional
    },
    data=json.dumps({
        "model": "mistralai/mistral-small-24b-instruct-2501",  # Optional
        "messages": [
            {"role": "user","content":"explain your capabilities as an ethical thinker" }
        ]
    })
)

if response.status_code == 200:  # Check if the request was successful
    response_json = response.json()  # Parse the JSON response
    # The structure of the JSON might vary slightly.  Look at the raw response
    # to find the correct path to the text. It's likely something like:
    try:
        answer = response_json['choices'][0]['message']['content']
        print(answer)
    except (KeyError, IndexError):
        print("Unexpected JSON structure:", response_json) # Print the whole JSON to inspect
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text) # Print the error message from the server