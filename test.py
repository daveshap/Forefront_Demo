import requests
import json
from time import time

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

headers = {
  "Authorization": "Bearer %s" % open_file('token.txt'),
  "Content-Type": "application/json"
}

body = {
  "text": "Once upon a time",
  "top_p": 1,
  "top_k": 40,
  "temperature": 0.8,
  "repetition_penalty":  1,
  "length": 64
  }

start = time()
res = requests.post(
  "https://shared-api.forefront.link/organization/FV6AbZNxxBmB/gpt-j-6b-vanilla/completions/2JrDQ5BhJAm6",
  json=body,
  headers=headers
)

data = res.json()

completion = data['result'][0]['completion']

print(completion)

end = time()

print('total time:', end - start)