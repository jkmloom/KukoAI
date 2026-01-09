# import os
# from Config import apikey
# from http.client import responses
# from openai import OpenAI
#
# client = OpenAI(
#     # This is the default and can be omitted
#     api_key=apikey,
# )
#
# response = client.responses.create(
#     model="gpt-4o",
#     instructions="You are a cool assistant that talks like a friend.",
#     input="Hey how's the weather today?",
# )
#
# print(response)

import os
import openai
from Config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to my boss for resignation?",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)