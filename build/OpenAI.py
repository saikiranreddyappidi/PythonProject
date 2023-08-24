import os
import openai
OPENAI_API_KEY="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"
openai.api_key = OPENAI_API_KEY
text="The CoAP protocol is designed for which applications"
arr=openai.Completion.create(
  model="text-davinci-003",
  prompt=text,
  max_tokens=1000,
  temperature=0
)
print(arr,type(arr))
print(arr["choices"][0]["text"])
# print(arr["choices"][0]["text"].split(" "))
# print(dict(arr))