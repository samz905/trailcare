from ollama import generate

print("Generating response...")
response = generate('gemma3n:e2b', "I’m hiking alone in a remote area. I slipped on wet rocks and landed hard. I felt a pop in my knee and now I can’t straighten or put weight on my leg. It’s swelling fast and extremely painful. I also dropped my backpack in a stream, so I’ve lost most of my supplies except a small first aid kit and a jacket. There’s no signal here. What should I do?")
print("Response generated.")
print(response['response'])
