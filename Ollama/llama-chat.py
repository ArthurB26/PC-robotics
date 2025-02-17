from ollama import chat
from ollama import ChatResponse

ainput = input("YOU: ")
response: ChatResponse = chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': ainput,
  },
])
print(response.message.content)
